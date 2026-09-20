# utils/generate_icons.py
# Generates razor-sharp, premium icons for CheatCode at 16, 32, 48, 128 px
# Optimized specifically for each resolution:
# - 16px: High-contrast, bold geometry so it pops on Chrome toolbar
# - 32px: Crisp retina toolbar icon with sharp anti-aliasing
# - 48px: Medium extension manager icon with refined borders
# - 128px: Store-quality asset with sleek dark glassmorphic styling and vibrant brand accents

import os
from PIL import Image, ImageDraw, ImageFilter

def create_16px():
    scale = 4
    size = 16 * scale
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    
    pad = 2
    r = int(size * 0.22)
    d.rounded_rectangle([pad, pad, size - pad, size - pad], radius=r, fill=(16, 17, 22, 255), outline=(52, 55, 68, 255), width=2)
    
    lw = 7
    cap_r = lw // 2
    
    # Left chevron in LeetCode Gold/Orange (#FFA116)
    pts = [(size*0.36, size*0.26), (size*0.16, size*0.50), (size*0.36, size*0.74)]
    d.line(pts, fill=(255, 161, 22, 255), width=lw)
    for p in pts: d.ellipse([p[0]-cap_r, p[1]-cap_r, p[0]+cap_r, p[1]+cap_r], fill=(255, 161, 22, 255))
    
    # Slash in Crisp White (#FFFFFF)
    s_pts = [(size*0.42, size*0.74), (size*0.58, size*0.26)]
    d.line(s_pts, fill=(255, 255, 255, 255), width=lw)
    for p in s_pts: d.ellipse([p[0]-cap_r, p[1]-cap_r, p[0]+cap_r, p[1]+cap_r], fill=(255, 255, 255, 255))
    
    # Right chevron in GFG Green (#22C55E)
    r_pts = [(size*0.64, size*0.26), (size*0.84, size*0.50), (size*0.64, size*0.74)]
    d.line(r_pts, fill=(34, 197, 94, 255), width=lw)
    for p in r_pts: d.ellipse([p[0]-cap_r, p[1]-cap_r, p[0]+cap_r, p[1]+cap_r], fill=(34, 197, 94, 255))
    
    out = img.resize((16, 16), Image.BOX)
    return out.filter(ImageFilter.UnsharpMask(radius=0.8, percent=150, threshold=2))

def create_32px():
    scale = 4
    size = 32 * scale
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    
    pad = 4
    r = int(size * 0.22)
    d.rounded_rectangle([pad, pad, size - pad, size - pad], radius=r, fill=(16, 17, 22, 255), outline=(50, 54, 68, 255), width=4)
    
    lw = 12
    cap_r = lw // 2
    
    # Left chevron
    pts = [(size*0.35, size*0.27), (size*0.17, size*0.50), (size*0.35, size*0.73)]
    d.line(pts, fill=(255, 161, 22, 255), width=lw)
    for p in pts: d.ellipse([p[0]-cap_r, p[1]-cap_r, p[0]+cap_r, p[1]+cap_r], fill=(255, 161, 22, 255))
    
    # Slash
    s_pts = [(size*0.43, size*0.73), (size*0.57, size*0.27)]
    d.line(s_pts, fill=(255, 255, 255, 255), width=lw)
    for p in s_pts: d.ellipse([p[0]-cap_r, p[1]-cap_r, p[0]+cap_r, p[1]+cap_r], fill=(255, 255, 255, 255))
    
    # Right chevron
    r_pts = [(size*0.65, size*0.27), (size*0.83, size*0.50), (size*0.65, size*0.73)]
    d.line(r_pts, fill=(34, 197, 94, 255), width=lw)
    for p in r_pts: d.ellipse([p[0]-cap_r, p[1]-cap_r, p[0]+cap_r, p[1]+cap_r], fill=(34, 197, 94, 255))
    
    out = img.resize((32, 32), Image.BOX)
    return out.filter(ImageFilter.UnsharpMask(radius=1.0, percent=140, threshold=2))

def create_48px():
    scale = 4
    size = 48 * scale
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    
    pad = 6
    r = int(size * 0.22)
    d.rounded_rectangle([pad, pad, size - pad, size - pad], radius=r, fill=(16, 17, 22, 255), outline=(52, 56, 72, 255), width=6)
    
    lw = 17
    cap_r = lw // 2
    
    pts = [(size*0.35, size*0.28), (size*0.18, size*0.50), (size*0.35, size*0.72)]
    d.line(pts, fill=(255, 161, 22, 255), width=lw)
    for p in pts: d.ellipse([p[0]-cap_r, p[1]-cap_r, p[0]+cap_r, p[1]+cap_r], fill=(255, 161, 22, 255))
    
    s_pts = [(size*0.43, size*0.72), (size*0.57, size*0.28)]
    d.line(s_pts, fill=(255, 255, 255, 255), width=lw)
    for p in s_pts: d.ellipse([p[0]-cap_r, p[1]-cap_r, p[0]+cap_r, p[1]+cap_r], fill=(255, 255, 255, 255))
    
    r_pts = [(size*0.65, size*0.28), (size*0.82, size*0.50), (size*0.65, size*0.72)]
    d.line(r_pts, fill=(34, 197, 94, 255), width=lw)
    for p in r_pts: d.ellipse([p[0]-cap_r, p[1]-cap_r, p[0]+cap_r, p[1]+cap_r], fill=(34, 197, 94, 255))
    
    out = img.resize((48, 48), Image.Resampling.BILINEAR)
    return out.filter(ImageFilter.UnsharpMask(radius=1.0, percent=120, threshold=2))

def create_128px():
    scale = 4
    size = 128 * scale
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    
    pad = 16
    r = int(size * 0.22)
    bbox = [pad, pad, size - pad, size - pad]
    
    # Base dark background
    d.rounded_rectangle(bbox, radius=r, fill=(15, 16, 21, 255))
    
    # Dual-tone accent border (LeetCode orange glow at top, subtle emerald at bottom)
    d.rounded_rectangle(bbox, radius=r, fill=None, outline=(56, 60, 78, 255), width=12)
    
    lw = 40
    cap_r = lw // 2
    
    # Left chevron '<' in LeetCode Gold/Orange (#FFA116)
    pts = [(size*0.35, size*0.28), (size*0.19, size*0.50), (size*0.35, size*0.72)]
    d.line(pts, fill=(255, 161, 22, 255), width=lw)
    for p in pts: d.ellipse([p[0]-cap_r, p[1]-cap_r, p[0]+cap_r, p[1]+cap_r], fill=(255, 161, 22, 255))
    
    # Center slash '/' in pure white
    s_pts = [(size*0.44, size*0.72), (size*0.56, size*0.28)]
    d.line(s_pts, fill=(245, 245, 250, 255), width=lw)
    for p in s_pts: d.ellipse([p[0]-cap_r, p[1]-cap_r, p[0]+cap_r, p[1]+cap_r], fill=(245, 245, 250, 255))
    
    # Right chevron '>' in GFG Green (#22C55E)
    r_pts = [(size*0.65, size*0.28), (size*0.81, size*0.50), (size*0.65, size*0.72)]
    d.line(r_pts, fill=(34, 197, 94, 255), width=lw)
    for p in r_pts: d.ellipse([p[0]-cap_r, p[1]-cap_r, p[0]+cap_r, p[1]+cap_r], fill=(34, 197, 94, 255))
    
    out = img.resize((128, 128), Image.Resampling.LANCZOS)
    return out.filter(ImageFilter.UnsharpMask(radius=1.2, percent=100, threshold=2))

def main():
    icons_dir = os.path.join(os.path.dirname(__file__), "..", "icons")
    os.makedirs(icons_dir, exist_ok=True)
    
    generators = {
        16: create_16px,
        32: create_32px,
        48: create_48px,
        128: create_128px
    }
    
    for s, gen in generators.items():
        icon = gen()
        path = os.path.join(icons_dir, f"icon{s}.png")
        icon.save(path, "PNG", optimize=True)
        print(f"Generated {path} ({s}x{s}px, custom-tuned)")

if __name__ == "__main__":
    main()
