# Vytvoříme bílý obrázek stejné velikosti jako nahraný obrázek a pomocí průměrného rozdílu pixelů do tohoto obrazku zakreslujeme pixely (hrany)

from PIL import Image, ImageDraw

def load_image(file_path):
    return Image.open(file_path)

def save_image(image, file_path):
    image.save(file_path)

# Funkce pro detekci krajů v obrázku
def detect_edges(image, threshold):
    width, height = image.size
    result_image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(result_image)

    for x in range(1, width - 1):
        for y in range(1, height - 1):
            current_pixel = image.getpixel((x, y))
            left_pixel = image.getpixel((x - 1, y))
            right_pixel = image.getpixel((x + 1, y))
            top_pixel = image.getpixel((x, y - 1))
            bottom_pixel = image.getpixel((x, y + 1))
            
            # Výpočet průměrného rozdílu pixelů 
            avg_difference = sum(abs(current_pixel[i] - neighbor[i]) for neighbor in [left_pixel, right_pixel, top_pixel, bottom_pixel] for i in range(3)) / 3
            
            # Pokud je rozdíl v hodnotách větší než threshold, nastavíme pixel na černou barvu
            if avg_difference > threshold:
                draw.point((x, y), fill="black")

    return result_image

def detection(input_path, output_path):
    threshold = int(input("Please enter a threshold between 0 and 100: "))
    while threshold < 0 or threshold > 100:
        print("Invalid threshold. Please enter a value between 0 and 100.")
        threshold = int(input("Enter threshold: "))

    input_image = load_image(input_path)

    edge_image = detect_edges(input_image, threshold)

    save_image(edge_image, output_path)


detection("input_image.jpg", "out_image.jpg")

