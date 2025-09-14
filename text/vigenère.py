import numpy as np
import random, string

def vigenere_encrypt(text, key):
    result = ""
    key = key.upper()
    key_index = 0
    for char in text.upper():
        if char.isalpha():
            shift = ord(key[key_index]) - 65
            result += chr((ord(char) - 65 + shift) % 26 + 65)
            key_index = (key_index + 1) % len(key)
        else:
            result += char
    return result

def vigenere_decrypt(cipher, key):
    result = ""
    key = key.upper()
    key_index = 0
    for char in cipher.upper():
        if char.isalpha():
            shift = ord(key[key_index]) - 65
            result += chr((ord(char) - 65 - shift) % 26 + 65)
            key_index = (key_index + 1) % len(key)
        else:
            result += char
    return result

def random_key(length):
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(length))

# Example
plain = "HELLO WORLD"
key = random_key(np.random.randint(0, 27))
encrypted = vigenere_encrypt(plain, key)
decrypted = vigenere_decrypt(encrypted, key)
print("Vigenere Encrypt:", encrypted)
print("Vigenere Decrypt:", decrypted)