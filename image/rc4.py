import numpy as np
import os, random, string
from typing import ByteString

# RC4 core
def rc4(data: ByteString, key: bytes) -> bytes:
    S = list(range(256))
    j = 0
    out = bytearray()

    # KSA (Key Scheduling Algorithm)
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]

    # PRGA (Pseudo-Random Generation Algorithm)
    i = j = 0
    for byte in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        out.append(byte ^ K)

    return bytes(out)

def random_key(length):
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(length))

# Encrypt & Decrypt file
def rc4_encrypt_file(src_path: str, dst_path: str, key: str):
    with open(src_path, "rb") as f:
        data = f.read()
    enc = rc4(data, key.encode("utf-8"))
    with open(dst_path, "wb") as f:
        f.write(enc)

def rc4_decrypt_file(src_path: str, dst_path: str, key: str):
    rc4_encrypt_file(src_path, dst_path, key)

# Example usage
base_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(base_dir, "decrypt.png")
encrypted_path = os.path.join(base_dir, "encrypt.enc")
decrypted_path = os.path.join(base_dir, "decrypt.png")
key = random_key(np.random.randint(1, 27))
rc4_encrypt_file(image_path, encrypted_path, key)
rc4_decrypt_file(encrypted_path, decrypted_path, key)