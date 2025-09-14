import random
import string

def substitution_encrypt(text, key):
    alphabet = string.ascii_uppercase
    table = str.maketrans(alphabet, key)
    return text.upper().translate(table)

def substitution_decrypt(cipher, key):
    alphabet = string.ascii_uppercase
    table = str.maketrans(key, alphabet)
    return cipher.upper().translate(table)

def random_substitution_key():
    letters = list(string.ascii_uppercase)
    random.shuffle(letters)
    return ''.join(letters)

# Example
key = random_substitution_key()
plain = "HELLO WORLD"
encrypted = substitution_encrypt(plain, key)
decrypted = substitution_decrypt(encrypted, key)
print("Substitution Encrypt:", encrypted)
print("Substitution Decrypt:", decrypted)