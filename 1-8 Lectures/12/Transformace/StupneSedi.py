from PIL import Image

def invert_colors(filename: str) -> None:
    image = Image.open(filename)
    inverted_image = image.convert('L')
    inverted_image.show()

invert_colors('image.jpg')