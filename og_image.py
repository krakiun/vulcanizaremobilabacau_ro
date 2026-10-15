#!/usr/bin/env python3
"""Generează imaginea de share (Facebook/WhatsApp) 1200x630: static/assets/og-image.png"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).parent / "static" / "assets" / "og-image.png"
F = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
W, H = 1200, 630
ORANGE, INK, MUTED = (249, 115, 22), (15, 23, 42), (100, 116, 139)

img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
# soft orange glow top-right
glow = Image.new("RGB", (W, H), "white")
gd = ImageDraw.Draw(glow)
for r in range(520, 0, -8):
    t = r / 520
    c = tuple(int(255 - (255 - v) * (1 - t) * 0.35) for v in (255, 237, 213))
    gd.ellipse((1050 - r, -150 - r, 1050 + r, -150 + r), fill=c)
img = Image.blend(img, glow, 1)
d = ImageDraw.Draw(img)

# tire illustration
cx, cy = 930, 330
d.ellipse((cx - 200, cy - 200, cx + 200, cy + 200), fill=(11, 15, 23))
d.ellipse((cx - 130, cy - 130, cx + 130, cy + 130), fill=(203, 213, 225))
d.ellipse((cx - 112, cy - 112, cx + 112, cy + 112), fill=(226, 232, 240))
import math
for k in range(5):
    a = math.radians(-90 + k * 72)
    d.line((cx + 30 * math.cos(a), cy + 30 * math.sin(a), cx + 100 * math.cos(a), cy + 100 * math.sin(a)), fill=(148, 163, 184), width=20)
d.ellipse((cx - 34, cy - 34, cx + 34, cy + 34), fill=ORANGE)
d.ellipse((cx - 12, cy - 12, cx + 12, cy + 12), fill="white")

f_pill = ImageFont.truetype(F, 26)
f_h = ImageFont.truetype(F, 78)
f_sub = ImageFont.truetype(F, 34)
f_tel = ImageFont.truetype(F, 58)

d.rounded_rectangle((70, 80, 325, 132), radius=26, fill="white", outline=(229, 231, 235), width=2)
d.ellipse((92, 98, 108, 114), fill=(22, 163, 74))
d.text((122, 92), "Non-stop 24/7", font=f_pill, fill=(51, 65, 85))
d.text((70, 170), "Vulcanizare", font=f_h, fill=INK)
d.text((70, 258), "Mobilă Bacău", font=f_h, fill=ORANGE)
d.text((70, 362), "Venim la tine: pană, montaj, echilibrare", font=f_sub, fill=MUTED)
d.rounded_rectangle((70, 450, 560, 548), radius=49, fill=ORANGE)
d.text((112, 467), "0756 492 992", font=f_tel, fill="white")

OUT.parent.mkdir(parents=True, exist_ok=True)
img.save(OUT, optimize=True)
print("OK ->", OUT)
