# Design Feedback App

A tool to support client feedback rounds on design work (starting with the HKBU Major Milestones infographic).

## Folders

- `feedback-board/` — `design_feedback_board.html`, a self-contained, no-install web page. Upload one or more design images, drag a box around anything that needs a change, leave a comment, and download the feedback as a JSON file to send back. This is the main tool.
- `assets/` — `id_map.png`, a color-coded wireframe map showing where each tagged element (e.g. `M1-YEAR`, `HDR-TITLE-EN`) sits on the HKBU Milestones design.
- `scripts/` — `elements.py` (the element registry: IDs, positions, current text) and `make_wireframe.py` (builds `id_map.png` from it).
- `tests/` — `test_tool.py`, an automated browser test for the feedback board (upload, drag-select, comment, export/import round-trip).

## How it fits together

The HTML feedback board in `feedback-board/` is the main deliverable — it lets a non-designer client mark up any number of design images directly and send back a JSON file with their comments, without needing Excel or design software.
