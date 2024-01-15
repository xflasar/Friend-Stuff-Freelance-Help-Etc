from PIL import Image, ImageDraw
import math

def triangle(size: int = 150, a: int = 50) -> None:
    img = Image.new("RGB", (size, size), "white")
    draw = ImageDraw.Draw(img)

    height = int(math.sqrt(3) / 2 * a)
    x1 = (size - a) // 2
    y1 = (size + height) // 2
    
    x2 = x1 + a
    y2 = y1

    x3 = (size - a) // 2 + a // 2
    y3 = y1 - height

    draw.polygon([(x1, y1), (x2, y2), (x3, y3)], fill="black")

    img.show()

triangle()