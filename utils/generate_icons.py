# utils/generate_icons.py
# Generates crisp, modern icons for CheatCode in 16, 32, 48, 128 px

import os
from PIL import Image, ImageDraw, ImageFont

def create_icon(size):
    # Create image with transparent background
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Padding and rounded rectangle bounds
    pad = max(1, int(size * 0.06))
    r = int(size * 0.22)
    bbox = [pad, pad, size - pad, size - pad]

    # Draw dark slate rounded rectangle
    draw.rounded_rectangle(bbox, radius=r, fill=(24, 24, 27, 255), outline=(255, 161, 22, 230), width=max(1, int(size * 0.04)))

    # Draw stylized code symbols or brackets
    # For small sizes (16, 32), draw clean geometric shapes
    # Left chevron '<' in LeetCode Orange (#FFA116)
    # Right chevron '>' in GFG Green (#22C55E)
    # Slash '/' in Silver (#E4E4E7)

    w = size
    h = size
    lw = max(1.5, size * 0.08)

    # Left chevron '<'
    left_pts = [
        (w * 0.38, h * 0.32),
        (w * 0.24, h * 0.50),
        (w * 0.38, h * 0.68)
    ]
    draw.line(left_pts, fill=(255, 161, 22, 255), width=int(lw), joint="curve")

    # Center slash '/'
    slash_pts = [
        (w * 0.44, h * 0.70),
        (w * 0.56, h * 0.30)
    ]
    draw.line(slash_pts, fill=(244, 244, 245, 240), width=int(lw))

    # Right chevron '>'
    right_pts = [
        (w * 0.62, h * 0.32),
        (w * 0.76, h * 0.50),
        (w * 0.62, h * 0.68)
    ]
    draw.line(right_pts, fill=(34, 197, 94, 255), width=int(lw), joint="curve")

    return img

def main():
    icons_dir = os.path.join(os.path.dirname(__file__), "..", "icons")
    os.makedirs(icons_dir, exist_ok=True)
    
    sizes = [16, 32, 48, 128]
    for s in sizes:
        icon = create_icon(s)
        path = os.path.join(icons_dir, f"icon{s}.png")
        icon.save(path, "PNG")
        print(f"Generated {path}")

if __name__ == "__main__":
    main()
