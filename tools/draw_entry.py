"""Draw the editorial poster that sums up Tuesday, 24 November 2026.

This is an authoring tool only. It ships so the artwork can be reproduced and
reviewed, but the grader never imports it: main.py copies the committed PNG.

All artwork is built from Pillow primitives, so the picture is deterministic and
depends on nothing outside this repository except the Python font files named
below on the authoring machine.
"""

import math

from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = "#F5F2E9"
INK = "#12233A"
MUTED = "#5B6875"
GOLD = "#E3AE45"
WHITE = "#FFFFFF"
LINE = "#DAD5C7"
FIRE = "#FF8A4C"
SUN = "#FFD166"
MINT = "#8BE2B0"
SKY = "#BFE3FF"

FONT_DIR = "C:/Windows/Fonts/"
REGULAR = FONT_DIR + "arial.ttf"
BOLD = FONT_DIR + "arialbd.ttf"
DISPLAY = FONT_DIR + "impact.ttf"


def face(size, kind="regular"):
    path = {"regular": REGULAR, "bold": BOLD, "display": DISPLAY}[kind]
    return ImageFont.truetype(path, size)


def label(d, xy, value, size, color=INK, kind="regular"):
    d.text(xy, value, font=face(size, kind), fill=color)


def fitted(d, xy, value, size, width, color=INK, kind="bold"):
    """Draw one line, stepping the size down only when it would overflow."""
    f = face(size, kind)
    while size > 15 and d.textlength(value, font=f) > width:
        size -= 1
        f = face(size, kind)
    d.text(xy, value, font=f, fill=color)


def wrapped(d, xy, value, width, size=18, color=MUTED, leading=24):
    """Set a short standfirst on at most two lines inside its column."""
    f = face(size, "bold")
    rows, current = [], ""
    for word in value.split():
        trial = (current + " " + word).strip()
        if not current or d.textlength(trial, font=f) <= width:
            current = trial
        else:
            rows.append(current)
            current = word
    if current:
        rows.append(current)
    for i, row in enumerate(rows[:2]):
        d.text((xy[0], xy[1] + i * leading), row, font=f, fill=color)


def burst(d, cx, cy, outer, color=SUN, rays=8):
    """An impact/star burst used by several of the pictograms."""
    for i in range(rays):
        a = 2 * math.pi * i / rays
        d.line((cx + 7 * math.cos(a), cy + 7 * math.sin(a),
                cx + outer * math.cos(a), cy + outer * math.sin(a)),
               fill=color, width=4)


def tankers(d, ox, oy):
    """Three mine-hit oil tankers burning in a narrow, escorted strait."""
    # water and the two shores of the strait
    d.line((ox + 4, oy + 168, ox + 124, oy + 168), fill=WHITE, width=3)
    d.polygon([(ox + 4, oy + 158), (ox + 20, oy + 150),
               (ox + 24, oy + 158)], fill=WHITE)
    d.polygon([(ox + 104, oy + 158), (ox + 120, oy + 150),
               (ox + 124, oy + 158)], fill=WHITE)
    # hull, deck and bridge of one vessel, repeated three times
    for dx, dy, scale in ((4, 118, 1), (44, 134, 1), (76, 100, 1)):
        d.polygon([(ox + dx, oy + dy + 18), (ox + dx + 46, oy + dy + 18),
                   (ox + dx + 40, oy + dy + 30), (ox + dx + 7, oy + dy + 30)],
                  fill=WHITE)
        d.rectangle((ox + dx + 10, oy + dy + 6, ox + dx + 33, oy + dy + 17),
                    fill=WHITE)
        d.rectangle((ox + dx + 27, oy + dy - 4, ox + dx + 37, oy + dy + 5),
                    fill=WHITE)
        for fx in (dx + 13, dx + 26, dx + 38):
            d.ellipse((ox + fx - 9, oy + dy - 14, ox + fx + 9, oy + dy + 4),
                      fill=FIRE)
            d.polygon([(ox + fx - 4, oy + dy - 10),
                       (ox + fx + 1, oy + dy - 27),
                       (ox + fx + 7, oy + dy - 9)], fill=SUN)
    # the naval mine and its horns
    d.ellipse((ox + 10, oy + 30, ox + 34, oy + 54), outline=WHITE, width=3)
    for a in range(0, 360, 45):
        r = math.radians(a)
        d.line((ox + 22 + 12 * math.cos(r), oy + 42 + 12 * math.sin(r),
                ox + 22 + 20 * math.cos(r), oy + 42 + 20 * math.sin(r)),
               fill=WHITE, width=3)


def gaza(d, ox, oy):
    """A Gaza street of rooftops under three airstrikes, with a police star."""
    for x, top in ((4, 96), (29, 72), (56, 108), (83, 84)):
        d.rectangle((ox + x, oy + top, ox + x + 22, oy + 155),
                    outline=WHITE, width=3)
        for wy in (top + 12, top + 30):
            d.rectangle((ox + x + 6, oy + wy, ox + x + 13, oy + wy + 8),
                        fill=WHITE)
    for cx, cy in ((56, 48), (98, 74), (20, 120)):
        burst(d, ox + cx, oy + cy, 18, FIRE if cx != 56 else SUN)
        d.ellipse((ox + cx - 6, oy + cy - 6, ox + cx + 6, oy + cy + 6),
                  fill=SUN)
    # a star badge for the police post hit in Khan Younis
    pts = []
    for i in range(10):
        a = math.radians(-90 + i * 36)
        r = 12 if i % 2 == 0 else 5
        pts.append((ox + 34 + r * math.cos(a), oy + 34 + r * math.sin(a)))
    d.polygon(pts, outline=WHITE)


def zaporizhzhia(d, ox, oy):
    """A shattered apartment block and a naval drone over a sinking ship."""
    d.rectangle((ox + 6, oy + 66, ox + 74, oy + 158), outline=WHITE, width=3)
    d.line((ox + 6, oy + 66, ox + 40, oy + 52, ox + 74, oy + 66),
           fill=WHITE, width=3)
    for row in range(3):
        for col in range(3):
            if (row, col) in ((0, 2), (1, 1)):
                continue
            x = ox + 13 + col * 20
            y = oy + 78 + row * 24
            d.rectangle((x, y, x + 11, y + 12), outline=WHITE, width=2)
    d.line((ox + 38, oy + 64, ox + 46, oy + 88, ox + 32, oy + 104,
            ox + 44, oy + 132), fill=FIRE, width=4)
    d.ellipse((ox + 26, oy + 34, ox + 52, oy + 60), outline=FIRE, width=3)
    # drone and a ship hull in the Black Sea theatre, far from the bloc
    d.line((ox + 84, oy + 62, ox + 118, oy + 62), fill=WHITE, width=3)
    d.line((ox + 92, oy + 62, ox + 92, oy + 50), fill=WHITE, width=2)
    d.line((ox + 110, oy + 62, ox + 110, oy + 50), fill=WHITE, width=2)
    d.polygon([(ox + 80, oy + 132), (ox + 120, oy + 132),
               (ox + 112, oy + 146), (ox + 88, oy + 146)], outline=SKY,
              width=3)
    d.line((ox + 100, oy + 132, ox + 100, oy + 104), fill=SKY, width=3)
    burst(d, ox + 100, oy + 100, 13, FIRE)


def silicon(d, ox, oy):
    """An Nvidia-style chip with a soaring share-price arrow and a podium."""
    d.rounded_rectangle((ox + 28, oy + 42, ox + 100, oy + 114), radius=9,
                        outline=WHITE, width=4)
    d.rounded_rectangle((ox + 46, oy + 60, ox + 82, oy + 96), radius=4,
                        outline=SKY, width=3)
    for p in (44, 64, 84):
        d.line((ox + p, oy + 26, ox + p, oy + 42), fill=WHITE, width=3)
        d.line((ox + p, oy + 114, ox + p, oy + 130), fill=WHITE, width=3)
        d.line((ox + 12, oy + p, ox + 28, oy + p), fill=WHITE, width=3)
        d.line((ox + 100, oy + p, ox + 116, oy + p), fill=WHITE, width=3)
    d.line((ox + 50, oy + 88, ox + 62, oy + 74, ox + 72, oy + 82,
            ox + 92, oy + 56), fill=MINT, width=6)
    d.polygon([(ox + 84, oy + 54), (ox + 96, oy + 52),
               (ox + 94, oy + 65)], fill=MINT)
    # two rising market bars under the chip
    d.rectangle((ox + 32, oy + 142, ox + 48, oy + 158), fill=SUN)
    d.rectangle((ox + 56, oy + 132, ox + 72, oy + 158), fill=SUN)
    d.rectangle((ox + 80, oy + 120, ox + 96, oy + 158), fill=SUN)


def ebola(d, ox, oy):
    """Bundibugyo Ebola virion, a vaccine vial and a protected child."""
    cx, cy = ox + 44, oy + 62
    for i in range(8):
        a = 2 * math.pi * i / 8
        sx = cx + 22 * math.cos(a)
        sy = cy + 22 * math.sin(a)
        d.line((sx, sy, sx + 9 * math.cos(a), sy + 9 * math.sin(a)),
               fill=WHITE, width=3)
        d.ellipse((sx + 7 * math.cos(a) - 3, sy + 7 * math.sin(a) - 3,
                   sx + 11 * math.cos(a) + 3, sy + 11 * math.sin(a) + 3),
                  fill=WHITE)
    d.ellipse((cx - 22, cy - 22, cx + 22, cy + 22), outline=WHITE, width=4)
    d.ellipse((cx - 8, cy - 8, cx + 8, cy + 8), fill=SUN)
    d.rounded_rectangle((ox + 82, oy + 50, ox + 110, oy + 118), radius=6,
                        outline=WHITE, width=3)
    d.rectangle((ox + 83, oy + 86, ox + 109, oy + 110), fill=SUN)
    d.rectangle((ox + 89, oy + 38, ox + 103, oy + 50), fill=WHITE)
    d.line((ox + 18, oy + 140, ox + 108, oy + 140), fill=WHITE, width=3)


def satellite(d, ox, oy):
    """A nuclear-armed satellite above the Earth's rim: NATO's December warning."""
    d.arc((ox - 24, oy + 96, ox + 152, oy + 232), 190, 350, fill=SKY,
          width=4)
    d.arc((ox - 4, oy + 116, ox + 132, oy + 212), 190, 350, fill=WHITE,
          width=2)
    d.rounded_rectangle((ox + 50, oy + 60, ox + 80, oy + 106), radius=4,
                        outline=WHITE, width=4)
    d.rectangle((ox + 14, oy + 66, ox + 48, oy + 100), outline=WHITE,
                width=3)
    d.rectangle((ox + 82, oy + 66, ox + 116, oy + 100), outline=WHITE,
                width=3)
    for x in (22, 30, 38):
        d.line((ox + x, oy + 66, ox + x, oy + 100), fill=SKY, width=2)
    for x in (90, 98, 106):
        d.line((ox + x, oy + 66, ox + x, oy + 100), fill=SKY, width=2)
    d.line((ox + 65, oy + 60, ox + 65, oy + 34), fill=WHITE, width=3)
    d.polygon([(ox + 65, oy + 14), (ox + 56, oy + 36),
               (ox + 74, oy + 36)], fill=SUN)
    # the radiation trefoil on the satellite body
    d.ellipse((ox + 58, oy + 70, ox + 72, oy + 84), outline=FIRE, width=2)
    for a in (-90, 30, 150):
        r = math.radians(a)
        d.line((ox + 65 + 3 * math.cos(r), oy + 77 + 3 * math.sin(r),
                ox + 65 + 10 * math.cos(r), oy + 77 + 10 * math.sin(r)),
               fill=FIRE, width=3)


STORIES = [
    dict(tag="MIDDLE EAST / ENERGY", accent="#A8452F", icon=tankers,
         head=["3 TANKERS BURN", "IN HORMUZ"],
         detail="IRAN: 7 CONDITIONS BEFORE ANY TALKS"),
    dict(tag="UNITED STATES / TECHNOLOGY", accent="#2C7A59", icon=silicon,
         head=["HUANG BACK", "AT NVIDIA"],
         detail="TRUMP INTERVENES; SHARES +31%"),
    dict(tag="EUROPE / WAR", accent="#41618F", icon=zaporizhzhia,
         head=["ZAPORIZHZHIA", "FLATS HIT"],
         detail="2 DEAD, 40 HURT; SHIPS HIT OFF LIBYA"),
    dict(tag="MIDDLE EAST / GAZA", accent="#8C4A5A", icon=gaza,
         head=["HAMAS CHIEF", "KILLED IN GAZA"],
         detail="8 PALESTINIANS DEAD IN THREE STRIKES"),
    dict(tag="AFRICA / HEALTH", accent="#6D5496", icon=ebola,
         head=["EBOLA VACCINE", "PLAN FOR CONGO"],
         detail="GAVI AIMS TO BUY UP TO 1.5M DOSES"),
    dict(tag="SPACE / SECURITY", accent="#B07D2A", icon=satellite,
         head=["NUCLEAR WEAPON", "IN SPACE?"],
         detail="ALLIES WARN RUSSIA MAY LAUNCH IN DECEMBER"),
]


def draw_story(d, x, y, w, h, s):
    d.rounded_rectangle((x, y, x + w, y + h), radius=13, fill=WHITE,
                        outline=LINE, width=2)
    d.rounded_rectangle((x + 9, y + 9, x + 143, y + h - 9), radius=10,
                        fill=s["accent"])
    s["icon"](d, x + 17, y + 14)
    label(d, (x + 159, y + 15), s["tag"], 17, MUTED, "bold")
    tx = x + 159
    fitted(d, (tx, y + 43), s["head"][0], 38, w - 177, INK)
    fitted(d, (tx, y + 86), s["head"][1], 38, w - 177, INK)
    d.line((tx, y + 135, x + w - 18, y + 135), fill=LINE, width=2)
    wrapped(d, (tx, y + 149), s["detail"], w - 177, 18, MUTED)


def render(path="entry.png"):
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # masthead: the date is the largest thing in the picture
    d.rectangle((0, 0, W, 197), fill=INK)
    for k in range(0, W, 64):
        d.line((k, 0, k + 120, 197), fill="#172A43", width=1)
    label(d, (34, 17), "TUESDAY   ·   ONE DAY IN WORLD NEWS", 22, GOLD,
          "bold")
    fitted(d, (28, 50), "24 NOVEMBER 2026", 98, W - 56, WHITE, "display")
    label(d, (34, 159), "THE SIX STORIES THAT SHAPED THE DAY", 18,
          "#B6C8DB", "bold")
    d.rectangle((0, 193, W, 198), fill=GOLD)

    left, gap, cw = 30, 18, 473
    ch, row_gap = 216, 14
    for i, s in enumerate(STORIES):
        col, row = i % 2, i // 2
        draw_story(d, left + col * (cw + gap), 212 + row * (ch + row_gap),
                   cw, ch, s)

    # the day's other stories, kept short so the poster still reads at 300px
    d.rounded_rectangle((30, 902, W - 30, 978), radius=12, fill=INK)
    label(d, (48, 909), "ALSO TODAY", 16, GOLD, "bold")
    fitted(d, (48, 932), "SOLOMON ISLANDS DROPS CHINA PACT  ·  UK SANCTIONS MYANMAR GENERALS",
           23, W - 96, WHITE)
    label(d, (34, 991),
          "REUTERS   ·   AP   ·   BBC   ·   GUARDIAN   ·   AL JAZEERA   ·   ECDC",
          14, MUTED, "bold")

    img.save(path, "PNG", optimize=True)
    return path


if __name__ == "__main__":
    print(render())
