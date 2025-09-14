import numpy as np
import random, string

def xor_encrypt(plaintext: bytes, key: bytes) -> bytes:
    klen = len(key)
    return bytes([b ^ key[i % klen] for i, b in enumerate(plaintext)])

def random_key(length):
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(length))

# Example
plain = b"HELLO WORLD"
key = random_key(np.random.randint(1, 27)).encode("utf-8")
encrypted = xor_encrypt(plain, key).hex()
decrypted = xor_encrypt(bytes.fromhex(encrypted), key)
print("XOR Encrypt:", encrypted)
print("XOR Decrypt:", decrypted)