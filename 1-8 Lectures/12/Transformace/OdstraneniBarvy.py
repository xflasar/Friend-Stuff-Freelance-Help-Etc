from PIL import Image

def without_green(filename: str) -> None:
  image = Image.open(filename)
  pixels = image.load()
  width, height = image.size

  for x in range(width):
    for y in range(height):
      r, g, b = pixels[x, y]
      pixels[x, y] = (r, 0, b)
  
  image.show()

without_green("image.jpg")