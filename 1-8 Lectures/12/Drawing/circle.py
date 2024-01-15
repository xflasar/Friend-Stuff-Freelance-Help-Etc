from PIL import Image, ImageDraw
from typing import Tuple

def circle(size: int = 150, center: Tuple[int, int] = (75, 75), radius: int = 20) -> None:
    img = Image.new("RGB", (size, size), "white")
    draw = ImageDraw.Draw(img)

    draw.ellipse([(center[0] - radius, center[1] - radius), (center[0] + radius, center[1] + radius)], outline="black", fill="black")

    img.show()

circle()