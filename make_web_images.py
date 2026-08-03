#!/usr/bin/env python3
"""
Regenerate web-optimized gallery JPGs from the master PNGs.
Masters:  images/spoolmojo_<n>.png  (kept local, gitignored)
Output:   images/web/spoolmojo_<n>.jpg  (committed, served by the site)

Run from the repo root:  python3 make_web_images.py
Only rebuilds JPGs that are missing or older than their master.
"""
import glob, os, re
from PIL import Image

MAX_SIDE, QUALITY = 1200, 82
os.makedirs('images/web', exist_ok=True)

done = skipped = 0
for src in sorted(glob.glob('images/spoolmojo_*.png'),
                  key=lambda f: int(re.search(r'_(\d+)\.png$', f).group(1))):
    n = re.search(r'_(\d+)\.png$', src).group(1)
    out = f'images/web/spoolmojo_{n}.jpg'
    if os.path.exists(out) and os.path.getmtime(out) >= os.path.getmtime(src):
        skipped += 1
        continue
    im = Image.open(src).convert('RGB')
    w, h = im.size
    scale = MAX_SIDE / max(w, h)
    if scale < 1:
        im = im.resize((round(w * scale), round(h * scale)), Image.LANCZOS)
    im.save(out, 'JPEG', quality=QUALITY, progressive=True, optimize=True)
    print(f'{src} {w}x{h} -> {out} {im.size[0]}x{im.size[1]} {os.path.getsize(out)//1024}KB')
    done += 1

print(f'{done} regenerated, {skipped} up to date')
