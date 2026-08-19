from PIL import Image, ImageDraw, ImageFont
from elements import elements, COLORS, CANVAS_W, CANVAS_H

SCALE = 1.0
W, H = int(CANVAS_W * SCALE), int(CANVAS_H * SCALE)

img = Image.new("RGB", (W, H), (250, 250, 248))
draw = ImageDraw.Draw(img)

font_label = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 13)
font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 11)
font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 20)

# Title
draw.text((16, 12), "HKBU Milestones — Element ID Map", font=font_title, fill=(20, 20, 20))
draw.text((16, 38), "Matches the ID tags now saved inside the Affinity layer names.", font=font_small, fill=(90, 90, 90))

top_offset = 60

for el in elements:
    x, y, w, h = el["box"]
    x *= SCALE; y = y * SCALE + top_offset; w *= SCALE; h *= SCALE
    color = COLORS[el["type"]]
    # semi-transparent-looking fill via lighter tint
    fill = tuple(int(c + (255 - c) * 0.85) for c in color)
    draw.rectangle([x, y, x + w, y + h], outline=color, width=2, fill=fill)

    label = el["id"]
    tw = draw.textlength(label, font=font_label)
    lx, ly = x + 3, y + 3
    draw.rectangle([lx - 2, ly - 1, lx + tw + 2, ly + 15], fill=color)
    draw.text((lx, ly), label, font=font_label, fill=(255, 255, 255))

# legend
legend_y = H - 40
lx = 16
legend_items = [
    ("header", "Header / titles"),
    ("year", "Year + heading"),
    ("body-en", "English body text"),
    ("body-zh", "Chinese body text"),
    ("image", "Photo"),
]
for key, label in legend_items:
    c = COLORS[key]
    draw.rectangle([lx, legend_y, lx + 16, legend_y + 16], fill=c)
    draw.text((lx + 22, legend_y), label, font=font_small, fill=(30, 30, 30))
    lx += 22 + int(draw.textlength(label, font=font_small)) + 24

img = img.crop((0, 560, W, H))

import os
out_path = os.path.join(os.path.dirname(__file__), "..", "assets", "id_map.png")
img.save(out_path)
print("saved", img.size, "->", out_path)
