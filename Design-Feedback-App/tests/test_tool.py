import json, os
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HTML_PATH = os.path.join(ROOT, "feedback-board", "design_feedback_board.html")
IMG_PATH = os.path.join(ROOT, "assets", "id_map.png")
DOWNLOAD_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "downloads")
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

console_errors = []

def drag(page, img, x1, y1, x2, y2):
    box = img.bounding_box()
    page.mouse.move(box["x"] + box["width"] * x1, box["y"] + box["height"] * y1)
    page.mouse.down()
    page.mouse.move(box["x"] + box["width"] * x2, box["y"] + box["height"] * y2, steps=8)
    page.mouse.up()

with sync_playwright() as p:
    browser = p.chromium.launch(executable_path="/opt/pw-browsers/chromium")
    context = browser.new_context(accept_downloads=True)
    page = context.new_page()
    page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)
    page.on("pageerror", lambda exc: console_errors.append(str(exc)))

    page.goto("file://" + HTML_PATH)

    # Upload two images (reuse same file twice to simulate two designs)
    page.set_input_files("#fileInput", [IMG_PATH, IMG_PATH])
    page.wait_for_timeout(500)

    tabs = page.query_selector_all(".tab")
    print("tabs after upload:", len(tabs))
    assert len(tabs) == 2, "expected 2 design tabs"

    # Drag a real rectangle (re-query img each time since render() replaces the DOM node)
    drag(page, page.query_selector(".stage img"), 0.15, 0.10, 0.55, 0.25)
    page.wait_for_timeout(150)
    # Plain click (no drag) -> should create a small default box
    drag(page, page.query_selector(".stage img"), 0.6, 0.5, 0.6, 0.5)
    page.wait_for_timeout(150)
    # Another real drag
    drag(page, page.query_selector(".stage img"), 0.2, 0.7, 0.5, 0.85)
    page.wait_for_timeout(150)

    regions = page.query_selector_all(".region")
    cards = page.query_selector_all(".region-card")
    print("regions:", len(regions), "cards:", len(cards))
    assert len(regions) == 3 and len(cards) == 3

    # check the dragged region has a real (non-minimum) size vs the click region
    sizes = page.eval_on_selector_all(".region", "els => els.map(e => ({w: e.style.width, h: e.style.height}))")
    print("region sizes:", sizes)

    # Type into each card's textarea
    textareas = page.query_selector_all(".region-card textarea")
    for i, ta in enumerate(textareas):
        ta.fill(f"Test comment {i+1}")

    # General feedback
    page.fill("#generalFeedback", "Overall looks good, just tweak spacing.")

    # Rename the currently-active tab (the one with the 3 regions) via dblclick
    active_name = page.query_selector(".tab.active .name")
    active_name.dblclick()
    page.keyboard.press("Control+A")
    page.keyboard.type("HKBU v1 Test")
    page.keyboard.press("Enter")
    page.wait_for_timeout(200)

    # The tab that currently holds the 3 regions is whichever one is "active".
    active_tab = page.query_selector(".tab.active")
    all_tabs = page.query_selector_all(".tab")
    other_tab = [t for t in all_tabs if t != active_tab][0]

    other_tab.click()
    page.wait_for_timeout(200)
    cards2 = page.query_selector_all(".region-card")
    print("cards on the untouched design (should be 0):", len(cards2))
    assert len(cards2) == 0

    # go back to the design that has the 3 regions/comments
    for t in page.query_selector_all(".tab"):
        if "3" in t.inner_text():
            t.click()
            break
    page.wait_for_timeout(200)
    assert len(page.query_selector_all(".region-card")) == 3

    # Highlight sync check: click a region box, confirm matching card gets 'highlight'
    first_box = page.query_selector(".region")
    region_id = first_box.get_attribute("data-region")
    first_box.click()
    page.wait_for_timeout(150)
    card_classes = page.query_selector(f'.region-card[data-region="{region_id}"]').get_attribute("class")
    print("card classes after clicking its box:", card_classes)
    assert "highlight" in card_classes

    # Export and capture download
    with page.expect_download() as dl_info:
        page.click("#exportBtn")
    download = dl_info.value
    out_path = os.path.join(DOWNLOAD_DIR, download.suggested_filename)
    download.save_as(out_path)
    print("downloaded:", out_path)

    with open(out_path) as f:
        data = json.load(f)
    print("designs in export:", len(data["designs"]))
    target = next(d for d in data["designs"] if d["name"] == "HKBU v1 Test")
    other = next(d for d in data["designs"] if d is not target)
    print("target design regions:", len(target["regions"]))
    print("sample region:", target["regions"][0])
    print("general feedback:", target["general"])

    assert len(target["regions"]) == 3
    assert target["general"] == "Overall looks good, just tweak spacing."
    assert len(other["regions"]) == 0
    for r in target["regions"]:
        assert "wPct" in r and "hPct" in r and r["wPct"] > 0 and r["hPct"] > 0

    # Test import round-trip: reload page, import the exported JSON
    page.goto("file://" + HTML_PATH)
    page.set_input_files("#importInput", out_path)
    page.wait_for_timeout(500)
    tabs_after_import = page.query_selector_all(".tab")
    print("tabs after import:", len(tabs_after_import))
    assert len(tabs_after_import) == 2
    active_after_import = page.query_selector(".tab.active .name").inner_text()
    print("active tab after import:", active_after_import)
    cards_after_import = page.query_selector_all(".region-card")
    print("cards after import:", len(cards_after_import))
    if active_after_import == "HKBU v1 Test":
        assert len(cards_after_import) == 3
    else:
        assert len(cards_after_import) == 0

    browser.close()

print("\nCONSOLE ERRORS:", console_errors)
assert not console_errors, "There were console errors"
print("\nALL TESTS PASSED")
