from PIL import Image
import random

def encrypt_image(input_image_path, output_image_path, key):
    # Open the image
    img = Image.open(input_image_path)
    pixels = list(img.getdata())

    # Encrypt the image
    random.seed(key)
    encrypted_pixels = []
    for pixel in pixels:
        r, g, b = pixel
        encrypted_pixels.append((r ^ key, g ^ key, b ^ key))

    # Create a new image with the encrypted pixels
    encrypted_img = Image.new(img.mode, img.size)
    encrypted_img.putdata(encrypted_pixels)
    encrypted_img.save(output_image_path)
    print(f"Image encrypted and saved to {output_image_path}")

def decrypt_image(input_image_path, output_image_path, key):
    # Open the image
    img = Image.open(input_image_path)
    pixels = list(img.getdata())

    # Decrypt the image
    random.seed(key)
    decrypted_pixels = []
    for pixel in pixels:
        r, g, b = pixel
        decrypted_pixels.append((r ^ key, g ^ key, b ^ key))

    # Create a new image with the decrypted pixels
