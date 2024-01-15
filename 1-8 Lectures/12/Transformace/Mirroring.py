from PIL import Image
from PIL import ImageOps

def mirror_image(filename):

  image = Image.open(filename)

  width, height = image.size

  left_half = image.crop((0, 0, width // 2, height))

  mirr_left = ImageOps.mirror(left_half)

  mirr_image = Image.new('RGB', (width, height))
  mirr_image.paste(left_half, (0, 0))
  mirr_image.paste(mirr_left, (width // 2, 0))

  mirr_image.show()

mirror_image('image.jpg')