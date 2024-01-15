from PIL import Image
import PIL.ImageOps

def invert_colors(filename: str) -> None:
    image = Image.open(filename)
    inverted_image = PIL.ImageOps.invert(image)
    inverted_image.show()

invert_colors('image.jpg')