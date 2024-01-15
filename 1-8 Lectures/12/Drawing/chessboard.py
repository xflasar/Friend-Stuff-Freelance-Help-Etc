from PIL import Image, ImageDraw

def create_chessboard(size=150, stripe_width=30):
    img = Image.new("RGB", (size, size), "white")
    draw = ImageDraw.Draw(img)

    num_stripes = size // stripe_width

    for row in range(num_stripes):
        for col in range(num_stripes):
            if (row + col) % 2 == 0:
              continue
            
            color = "black"

            x1, y1 = col * stripe_width, row * stripe_width
            x2, y2 = x1 + stripe_width, y1 + stripe_width

            draw.rectangle([x1, y1, x2, y2], fill=color)

    img.show()

create_chessboard()
