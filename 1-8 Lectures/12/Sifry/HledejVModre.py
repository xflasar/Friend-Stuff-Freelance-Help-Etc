from PIL import Image

def find_in_blue(image_path):
    image = Image.open(image_path)

    rgb_image = image.convert("RGB")

    r, g, b = rgb_image.split()
    b.show()

find_in_blue("c1.jpg")
