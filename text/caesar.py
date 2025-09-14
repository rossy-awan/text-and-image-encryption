import numpy as np

def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def caesar_decrypt(cipher, shift):
    return caesar_encrypt(cipher, -shift)

# Example
plain = "HELLO WORLD"
key = np.random.randint(0, 27)
encrypted = caesar_encrypt(plain, key)
decrypted = caesar_decrypt(encrypted, key)
print("Caesar Encrypt:", encrypted)
print("Caesar Decrypt:", decrypted)