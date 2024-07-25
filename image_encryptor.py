from PIL import Image
import random


def swap_pixels(image):
    width, height = image.size
    pixels = image.load()
    
    for _ in range(10000): 
        x1, y1 = random.randint(0, width - 1), random.randint(0, height - 1)
        x2, y2 = random.randint(0, width - 1), random.randint(0, height - 1)
        
        pixels[x1, y1], pixels[x2, y2] = pixels[x2, y2], pixels[x1, y1]
    
    return image

def add_constant_to_pixels(image, constant=50):
    width, height = image.size
    pixels = image.load()
    
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            r = (r + constant) % 256
            g = (g + constant) % 256
            b = (b + constant) % 256
            pixels[x, y] = (r, g, b)
    
    return image

def encrypt_image(image_path, operation, *args):
    image = Image.open(image_path)
    
    if operation == 'swap':
        encrypted_image = swap_pixels(image)
    elif operation == 'add_constant':
        encrypted_image = add_constant_to_pixels(image, *args)
    else:
        raise ValueError("Unsupported operation. Use 'swap' or 'add_constant'.")
    
    encrypted_image.save('encrypted_image.jpeg', 'JPEG')
    print("Image encrypted and saved as 'encrypted_image.jpeg'")

if __name__ == "__main__":
    encrypt_image('encrypted_image.jpeg', 'swap')