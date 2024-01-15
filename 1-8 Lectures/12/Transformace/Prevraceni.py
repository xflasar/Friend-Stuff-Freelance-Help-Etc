from PIL import Image

def invert(filename: str) -> None:
    img = Image.open(filename)
    inverted_img = img.transpose(Image.FLIP_LEFT_RIGHT)
    inverted_img.show()

invert('image.jpg')