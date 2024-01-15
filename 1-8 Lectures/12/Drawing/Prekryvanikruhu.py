from PIL import Image, ImageDraw
import numpy as np

def draw_overlapping_filled_circles(circles, image_size=300):
    image = Image.new("RGB", (image_size, image_size), "white")
    draw = ImageDraw.Draw(image)

    overlap_counts = np.zeros((image_size, image_size))

    for center, radius in circles:
        bbox = (
            int(center[0] - radius-1),
            int(center[1] - radius-1),
            int(center[0] + radius+1),
            int(center[1] + radius+1)
        )

        draw.ellipse(bbox)

        for x in range(image_size):
            for y in range(image_size):
                if (x - center[0])**2 + (y - center[1])**2 <= radius**2:
                    overlap_counts[x, y] += 1

    for x in range(image_size):
        for y in range(image_size):
            if overlap_counts[x, y] % 2 == 1:
                pixel = image.getpixel((x, y))
                new_pixel = (255 - pixel[0], 255 - pixel[1], 255 - pixel[2])
                image.putpixel((x, y), new_pixel)

    return image

circles_list = [((100, 100), 50), ((150, 150), 40), ((180, 100), 40)]

result_image = draw_overlapping_filled_circles(circles_list)
result_image.show()
