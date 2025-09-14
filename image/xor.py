import numpy as np
import cv2, os

def encrypt_image(image_path, encrypted_image_path, key):
    np.random.seed(key)
    image = cv2.imread(image_path)
    noise = np.random.randint(0, 256, image.shape, dtype=np.uint8)
    xor_key = np.random.randint(0, 256, image.shape, dtype=np.uint8)
    encrypted_image = cv2.bitwise_xor(np.clip(image + noise, 0, 255), xor_key)
    cv2.imwrite(encrypted_image_path, encrypted_image)

def decrypt_image(encrypted_image_path, decrypted_image_path, key):
    np.random.seed(key)
    image = cv2.imread(encrypted_image_path)
    noise = np.random.randint(0, 256, image.shape, dtype=np.uint8)
    xor_key = np.random.randint(0, 256, image.shape, dtype=np.uint8)
    decrypted_image = np.clip(cv2.bitwise_xor(image, xor_key) - noise, 0, 255).astype(np.uint8)
    cv2.imwrite(decrypted_image_path, decrypted_image)

# Example
base_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(base_dir, "decrypt.png")
encrypted_image_path = os.path.join(base_dir, "encrypt.png")
decrypted_image_path = os.path.join(base_dir, "decrypt.png")
key = 1952036748
encrypt_image(image_path, encrypted_image_path, key)
decrypt_image(encrypted_image_path, decrypted_image_path, key)