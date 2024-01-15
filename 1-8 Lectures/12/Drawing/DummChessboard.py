from PIL import Image, ImageDraw, ImageFilter
import math

def draw_pattern(image_size, square_size, inversed):
    img = Image.new("RGBA", (image_size, image_size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    for i in range(image_size // square_size):
        for j in range(image_size // square_size):
            x, y = i * square_size, j * square_size
            if inversed:
              square_color = "white" if (i + j) % 2 == 0 else "black"
            else:
              square_color = "black" if (i + j) % 2 == 0 else "white"
            draw.rectangle([x, y, x + square_size, y + square_size], fill=square_color)


    return img

def apply_circular_mask(background, pattern, circle_radius):
    mask = Image.new("L", background.size, 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.ellipse([background.width // 2 - circle_radius, background.height // 2 - circle_radius,
                      background.width // 2 + circle_radius, background.height // 2 + circle_radius], fill=255)

    pattern.putalpha(mask)

    result = Image.alpha_composite(background.convert("RGBA"), pattern)

    return result

def main():
    background = Image.new("RGB", (500, 500), 'WHITE')

    square_size = 30

    original_pattern = draw_pattern(background.width, square_size, False)
    pattern1 = draw_pattern(background.width, square_size, True)
    pattern2 = draw_pattern(background.width, square_size, False)
    pattern3 = draw_pattern(background.width, square_size, True)

    result1 = apply_circular_mask(original_pattern, pattern1, 200)
    result2 = apply_circular_mask(result1, pattern2, 150)
    final_result = apply_circular_mask(result2, pattern3, 100)

    final_result.show()

if __name__ == "__main__":
    main()
