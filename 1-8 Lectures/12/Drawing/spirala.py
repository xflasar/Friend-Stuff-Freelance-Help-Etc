from PIL import Image, ImageDraw
import math

def spiral(size: int = 150, turn_inc: int = 5, tstep: float = 0.05) -> None:
    img = Image.new("RGB", (size, size), "white")
    draw = ImageDraw.Draw(img)

    x, y = size // 2, size // 2
    t = 0

    while t < 1000:
        t += tstep
        radius = 1 + turn_inc * t
        angle = t / 1 * math.pi
        x += int(radius * math.cos(angle))
        y += int(radius * math.sin(angle))
        draw.point((x, y), fill="black")

    img.show()

spiral()