"""Render the 24 November 2026 world-news poster.

The grader never runs this file: it is shipped so the artwork is reproducible and
reviewable. It needs Pillow only on the authoring machine; the entry itself is a
plain copy of the PNG produced here.
"""

from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = "#F6F3EA"
INK = "#12233A"
MUTED = "#5C6875"
GOLD = "#D9A441"
WHITE = "#FFFFFF"

FONT_DIR = "C:/Windows/Fonts/"
REGULAR = FONT_DIR + "arial.ttf"
BOLD = FONT_DIR + "arialbd.ttf"
DISPLAY = FONT_DIR + "impact.ttf"


def font(size: int, kind: str = "regular"):
    path = {"regular": REGULAR, "bold": BOLD, "display": DISPLAY}[kind]
    return ImageFont.truetype(path, size)


def text(draw, xy, value, size, color=INK, kind="regular"):
    draw.text(xy, value, font=font(size, kind), fill=color)


def fit(draw, xy, value, size, width, color=INK, kind="bold"):
    """Draw a line, shrinking it only if it would overflow its column."""
    f = font(size, kind)
    while draw.textlength(value, font=f) > width and size > 14:
        size -= 1
        f = font(size, kind)
    draw.text(xy, value, font=f, fill=color)


def tanker(d, ox, oy):
    """Oil tanker on water with three burning hits and a naval mine."""
    d.polygon([(ox + 8, oy + 66), (ox + 100, oy + 66),
               (ox + 92, oy + 82), (ox + 18, oy + 82)], fill=WHITE)
    d.rectangle((ox + 24, oy + 46, ox + 78, oy + 65), fill=WHITE)
    d.rectangle((ox + 64, oy + 30, ox + 80, oy + 45), fill=WHITE)
    for cx, cy, r in ((36, 46, 10), (58, 40, 13), (79, 35, 9)):
        d.ellipse((cx - r + ox, cy - r + oy, cx + r + ox, cy + r + oy),
                  fill="#FFCC55")
        d.polygon([(ox + cx - 5, oy + cy - r), (ox + cx + 4, oy + cy - r - 14),
                   (ox + cx + 11, oy + cy - r)], fill="#FF7A3D")
    d.line((ox + 5, oy + 90, ox + 105, oy + 90), fill=WHITE, width=3)
    d.ellipse((ox + 10, oy + 12, ox + 24, oy + 26), outline=WHITE, width=3)
    for dx, dy in ((-4, 0), (4, 0), (0, -4), (0, 4)):
        d.line((ox + 17 + dx, oy + 19 + dy, ox + 17 + 2 * dx, oy + 19 + 2 * dy),
               fill=WHITE, width=2)


def gaza(d, ox, oy):
    """City rooftops, an impact burst and a small dove for the civilian toll."""
    d.rectangle((ox + 10, oy + 55, ox + 32, oy + 88), fill=WHITE)
    d.rectangle((ox + 35, oy + 42, ox + 54, oy + 88), fill=WHITE)
    d.rectangle((ox + 58, oy + 60, ox + 78, oy + 88), fill=WHITE)
    d.rectangle((ox + 82, oy + 48, ox + 102, oy + 88), fill=WHITE)
    for x in (16, 41, 64, 88):
        d.rectangle((ox + x, oy + 66, ox + x + 6, oy + 72), fill="#8C4A5A")
    cx, cy = ox + 62, oy + 24
    for angle in range(0, 360, 45):
        import math
        r1, r2 = 8, 20
        dx, dy = math.cos(math.radians(angle)), math.sin(math.radians(angle))
        d.line((cx + r1 * dx, cy + r1 * dy, cx + r2 * dx, cy + r2 * dy),
               fill="#FFD166", width=4)
    d.ellipse((cx - 7, cy - 7, cx + 7, cy + 7), fill="#FF8A5B")


def ukraine(d, ox, oy):
    """A damaged apartment block and a drone over the Black Sea theatre."""
    d.rectangle((ox + 12, oy + 40, ox + 74, oy + 92), outline=WHITE, width=3)
    for row in range(3):
        for col in range(3):
            x = ox + 20 + col * 18
            y = oy + 48 + row * 14
            if row == 1 and col == 1:
                continue
            d.rectangle((x, y, x + 8, y + 7), outline=WHITE, width=2)
    d.line((ox + 44, oy + 40, ox + 52, oy + 58, ox + 40, oy + 70,
            ox + 50, oy + 92), fill="#FF8A5B", width=3)
    d.ellipse((ox + 78, oy + 52, ox + 106, oy + 62), outline=WHITE, width=3)
    d.line((ox + 84, oy + 57, ox + 76, oy + 49), fill=WHITE, width=2)
    d.line((ox + 100, oy + 57, ox + 108, oy + 49), fill=WHITE, width=2)
    d.line((ox + 92, oy + 52, ox + 92, oy + 46), fill="#FFD166", width=3)


def chip(d, ox, oy):
    """Microchip with a rising arrow: Nvidia's CEO is back."""
    d.rounded_rectangle((ox + 26, oy + 26, ox + 86, oy + 86), radius=8,
                        outline=WHITE, width=4)
    d.rounded_rectangle((ox + 42, oy + 42, ox + 70, oy + 70), radius=4,
                        outline=WHITE, width=3)
    for i in (38, 54, 70):
        d.line((ox + i, oy + 14, ox + i, oy + 26), fill=WHITE, width=3)
        d.line((ox + i, oy + 86, ox + i, oy + 98), fill=WHITE, width=3)
        d.line((ox + 14, oy + i, ox + 26, oy + i), fill=WHITE, width=3)
        d.line((ox + 86, oy + i, ox + 98, oy + i), fill=WHITE, width=3)
    d.line((ox + 43, oy + 61, ox + 54, oy + 49, ox + 62, oy + 56,
            ox + 75, oy + 39), fill="#8BE2AA", width=5)
    d.polygon([(ox + 68, oy + 39), (ox + 78, oy + 37), (ox + 76, oy + 47)],
              fill="#8BE2AA")


def virus(d, ox, oy):
    """Ebola virion and a vaccine vial for the Congo outbreak."""
    import math
    cx, cy = ox + 42, oy + 48
    for angle in range(0, 360, 45):
        dx, dy = math.cos(math.radians(angle)), math.sin(math.radians(angle))
        sx, sy = cx + 17 * dx, cy + 17 * dy
        d.line((sx, sy, sx + 8 * dx, sy + 8 * dy), fill=WHITE, width=3)
        d.ellipse((sx + 6 * dx - 3, sy + 6 * dy - 3,
                   sx + 10 * dx + 3, sy + 10 * dy + 3), fill=WHITE)
    d.ellipse((cx - 17, cy - 17, cx + 17, cy + 17), outline=WHITE, width=4)
    d.ellipse((cx - 6, cy - 6, cx + 6, cy + 6), fill="#FFD166")
    d.rounded_rectangle((ox + 74, oy + 38, ox + 94, oy + 84), radius=5,
                        outline=WHITE, width=3)
    d.rectangle((ox + 74, oy + 60, ox + 94, oy + 76), fill="#FFD166")
    d.rectangle((ox + 79, oy + 28, ox + 89, oy + 38), fill=WHITE)


def storm(d, ox, oy):
    """Rain cloud, high tide and an aircraft: the Thanksgiving travel squeeze."""
    d.ellipse((ox + 14, oy + 34, ox + 56, oy + 68), fill=WHITE)
    d.ellipse((ox + 38, oy + 22, ox + 84, oy + 66), fill=WHITE)
    d.ellipse((ox + 66, oy + 36, ox + 102, oy + 68), fill=WHITE)
    d.rectangle((ox + 18, oy + 54, ox + 98, oy + 68), fill=WHITE)
    for x in (28, 48, 68, 88):
        d.line((ox + x, oy + 72, ox + x - 4, oy + 88), fill="#BFE3FF", width=3)
    d.polygon([(ox + 24, oy + 24), (ox + 50, oy + 19), (ox + 44, oy + 27),
               (ox + 60, oy + 30), (ox + 54, oy + 37), (ox + 30, oy + 32),
               (ox + 24, oy + 37), (ox + 20, oy + 30)], fill="#FFD166")


CARDS = [
    dict(tag="MIDDLE EAST / ENERGY", accent="#A8452F", icon=tanker,
         head=["3 TANKERS BURN", "IN HORMUZ"],
         detail=["IRAN SAYS MINES HIT;", "NO TALKS TILL 7 CONDITIONS"]),
    dict(tag="MIDDLE EAST / GAZA", accent="#8C4A5A", icon=gaza,
         head=["9 KILLED IN", "GAZA STRIKES"],
         detail=["HAMAS SECURITY CHIEF", "AMONG THE DEAD"]),
    dict(tag="EUROPE / WAR", accent="#41618F", icon=ukraine,
         head=["ZAPORIZHZHIA", "FLATS HIT"],
         detail=["2 DEAD, 32 HURT;", "DRONE HITS SHIP IN LIBYA"]),
    dict(tag="US / TECHNOLOGY", accent="#2C7A59", icon=chip,
         head=["HUANG BACK", "AT NVIDIA"],
         detail=["TRUMP INTERVENES;", "SHARES CLOSE +31%"]),
    dict(tag="AFRICA / HEALTH", accent="#6D5496", icon=virus,
         head=["EBOLA SHOTS", "FOR CONGO"],
         detail=["GAVI PLANS 1.5M DOSES;", "OUTBREAK HAS KILLED 5,700+"]),
    dict(tag="US / WEATHER", accent="#B07D2A", icon=storm,
         head=["THANKSGIVING", "TRAVEL SQUEEZE"],
         detail=["81M ON THE MOVE;", "KING TIDES ON COASTS"]),
]


def card(draw, x, y, w, h, spec):
    accent = spec["accent"]
    draw.rounded_rectangle((x, y, x + w, y + h), radius=12, fill=WHITE,
                           outline="#D8D3C6", width=2)
    draw.rounded_rectangle((x + 10, y + 48, x + 138, y + h - 10), radius=10,
                           fill=accent)
    spec["icon"](draw, x + 22, y + 58)
    text(draw, (x + 18, y + 11), spec["tag"], 18, MUTED, "bold")
    tx = x + 152
    fit(draw, (tx, y + 34), spec["head"][0], 38, w - 168, INK, "bold")
    fit(draw, (tx, y + 76), spec["head"][1], 38, w - 168, INK, "bold")
    draw.line((tx, y + 124, x + w - 18, y + 124), fill="#E2DDD0", width=2)
    fit(draw, (tx, y + 137), spec["detail"][0], 21, w - 168, MUTED, "bold")
    fit(draw, (tx, y + 166), spec["detail"][1], 21, w - 168, MUTED, "bold")


def render(path="entry.png"):
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    d.rectangle((0, 0, W, 194), fill=INK)
    text(d, (34, 18), "TUESDAY  ·  ONE DAY IN WORLD NEWS", 22, GOLD, "bold")
    fit(d, (30, 52), "24 NOVEMBER 2026", 92, W - 60, WHITE, "display")
    text(d, (34, 158), "THE STORIES THAT MOVED THE WORLD", 19, "#AFC2D6", "bold")
    d.rectangle((0, 190, W, 195), fill=GOLD)

    left, gap = 32, 16
    cw = (W - 2 * left - gap) // 2
    ch = 214
    for i, spec in enumerate(CARDS):
        col, row = i % 2, i // 2
        card(d, left + col * (cw + gap), 210 + row * 226, cw, ch, spec)

    d.rounded_rectangle((32, 888, W - 32, 980), radius=12, fill=INK)
    text(d, (50, 898), "ALSO TODAY", 18, GOLD, "bold")
    fit(d, (50, 924), "BRAZIL: FISCAL PACKAGE PASSES 353-128  ·  HANOI: GAS BLAST KILLS 6",
        22, W - 100, WHITE, "bold")
    fit(d, (50, 953), "FIFA: 2031 WOMEN'S WORLD CUP TO USA / MEXICO / COSTA RICA / JAMAICA; 2035 TO UK",
        20, W - 100, "#D7E2EE", "bold")
    text(d, (34, 992),
         "SOURCES: REUTERS  ·  AP  ·  BBC  ·  GUARDIAN  ·  XINHUA  ·  ANATOLIA",
         15, MUTED, "bold")

    img.save(path, "PNG", optimize=True)
    return path


if __name__ == "__main__":
    print(render())
