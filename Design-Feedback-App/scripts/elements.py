# Element registry for the HKBU Major Milestones infographic.
# Boxes extracted directly from the Affinity document's node tree (spreadBaseBox),
# canvas size 793 x 1983 (points).

CANVAS_W = 793
CANVAS_H = 1983

# type -> color (RGB)
COLORS = {
    "header": (52, 88, 176),      # blue
    "year": (219, 111, 27),       # orange
    "body-en": (43, 140, 92),     # green
    "body-zh": (23, 111, 140),    # teal
    "image": (140, 60, 150),      # purple
}

elements = [
    # id, type, box(x,y,w,h), section label, EN content, ZH content
    dict(id="HDR-NAME-ZH", type="header", box=(127.98, 580.09, 143.71, 16.88), section="Header",
         en="", zh="香港浸會大學"),
    dict(id="HDR-NAME-EN", type="header", box=(128.20, 609.07, 256.66, 11.11), section="Header",
         en="HONG KONG BAPTIST UNIVERSITY", zh=""),
    dict(id="HDR-TITLE-EN", type="header", box=(65.37, 671.51, 620.82, 34.07), section="Header",
         en="HKBU MAJOR MILESTONES", zh=""),
    dict(id="HDR-TITLE-ZH", type="header", box=(66.64, 722.16, 336.30, 28.13), section="Header",
         en="", zh="香港浸會大學重要里程碑"),

    dict(id="M1-YEAR", type="year", box=(382.92, 795.13, 228.36, 26.31), section="1956 — Foundation",
         en="1956 — FOUNDATION", zh=""),
    dict(id="M1-BODY-EN", type="body-en", box=(382.15, 840.35, 274.98, 61.02), section="1956 — Foundation",
         en="The Baptist Convention of Hong Kong founded Hong Kong Baptist College as a private post-secondary institution.", zh=""),
    dict(id="M1-BODY-ZH", type="body-zh", box=(382.75, 911.75, 197.08, 42.06), section="1956 — Foundation",
         en="", zh="香港浸信會聯會創辦私立專上學院「香港浸會書院」。"),
    dict(id="M1-IMAGE", type="image", box=(67.05, 800.5, 219, 191), section="1956 — Foundation",
         en="[photo]", zh=""),

    dict(id="M2-YEAR", type="year", box=(78.92, 1030.13, 358.09, 26.31), section="1966 — Waterloo Road Campus",
         en="1966 — WATERLOO ROAD CAMPUS", zh=""),
    dict(id="M2-BODY-EN", type="body-en", box=(77.20, 1073.35, 259.89, 37.83), section="1966 — Waterloo Road Campus",
         en="The College's permanent campus on Waterloo Road was completed.", zh=""),
    dict(id="M2-BODY-ZH", type="body-zh", box=(77.88, 1127.75, 173.75, 41.88), section="1966 — Waterloo Road Campus",
         en="", zh="浸會書院位於窩打老道的永久校舍落成。"),
    dict(id="M2-IMAGE", type="image", box=(520.64, 1003.36, 214, 185), section="1966 — Waterloo Road Campus",
         en="[photo]", zh=""),

    dict(id="M3-YEAR", type="year", box=(385.92, 1228.13, 295.82, 26.31), section="1994 — University Status",
         en="1994 — UNIVERSITY STATUS", zh=""),
    dict(id="M3-BODY-EN", type="body-en", box=(384.53, 1274.35, 223.88, 61.02), section="1994 — University Status",
         en="Hong Kong Baptist College was officially renamed Hong Kong Baptist University.", zh=""),
    dict(id="M3-BODY-ZH", type="body-zh", box=(384.88, 1346.75, 174.44, 42.0), section="1994 — University Status",
         en="", zh="香港浸會書院正式正名為香港浸會大學。"),
    dict(id="M3-IMAGE", type="image", box=(78.20, 1216.62, 229, 190), section="1994 — University Status",
         en="[photo]", zh=""),

    dict(id="M4-YEAR", type="year", box=(77.49, 1459.13, 306.14, 54.11), section="1997 — Baptist University Road Campus",
         en="1997 — BAPTIST UNIVERSITY ROAD CAMPUS", zh=""),
    dict(id="M4-BODY-EN", type="body-en", box=(78.38, 1529.55, 196.77, 37.63), section="1997 — Baptist University Road Campus",
         en="The Baptist University Road Campus was established.", zh=""),
    dict(id="M4-BODY-ZH", type="body-zh", box=(78.88, 1583.75, 148.96, 15), section="1997 — Baptist University Road Campus",
         en="", zh="浸會大學道校園落成。"),
    dict(id="M4-IMAGE", type="image", box=(509.45, 1427.41, 219, 202), section="1997 — Baptist University Road Campus",
         en="[photo]", zh=""),

    dict(id="M5-YEAR", type="year", box=(382.09, 1675.13, 265.23, 26.31), section="2005 — Kai Tak Campus",
         en="2005 — KAI TAK CAMPUS", zh=""),
    dict(id="M5-BODY-EN", type="body-en", box=(383.05, 1720.35, 295.27, 57.84), section="2005 — Kai Tak Campus",
         en="The Kai Tak Campus on Kwun Tong Road was established to house the Academy of Visual Arts.", zh=""),
    dict(id="M5-BODY-ZH", type="body-zh", box=(383.5, 1798.81, 195.94, 41.88), section="2005 — Kai Tak Campus",
         en="", zh="位於觀塘道的啟德校園落成，並成立視覺藝術院。"),
    dict(id="M5-IMAGE", type="image", box=(69, 1645, 228, 200), section="2005 — Kai Tak Campus",
         en="[photo]", zh=""),
]
