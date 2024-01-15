from PIL import Image, ImageDraw

def square(size: int = 250, a: int = 70) -> None:
    img = Image.new("RGB", (size, size), "white")
    draw = ImageDraw.Draw(img)

    left = (size - a) // 2
    top = (size - a) // 2
    right = left + a
    bottom = top + a

    draw.rectangle([left, top, right, bottom], fill="black")

    img.show()

square()