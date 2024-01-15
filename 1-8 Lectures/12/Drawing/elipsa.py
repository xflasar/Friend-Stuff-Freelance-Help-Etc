from PIL import Image, ImageDraw

def ellipse(size: int = 150, radius_a: int = 50, radius_b: int = 20) -> None:
    img = Image.new("RGB", (size, size), "white")
    draw = ImageDraw.Draw(img)

    draw.ellipse((radius_a, radius_b, size - radius_a, size - radius_b), fill="black")

    img.show()

ellipse()