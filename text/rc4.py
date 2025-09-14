import numpy as np
import random, string

def rc4_init(key: bytes):
    # Key Scheduling Algorithm
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) & 0xFF
        S[i], S[j] = S[j], S[i]
    return S

def rc4_stream(key: bytes, length: int):
    S = rc4_init(key)
    i = j = 0
    out = bytearray()
    for _ in range(length):
        i = (i + 1) & 0xFF
        j = (j + S[i]) & 0xFF
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) & 0xFF]
        out.append(K)
    return bytes(out)

def rc4_encrypt(plaintext: bytes, key: bytes) -> bytes:
    keystream = rc4_stream(key, len(plaintext))
    return bytes([p ^ k for p, k in zip(plaintext, keystream)])

def random_key(length):
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(length))

# Example
plain = b"HELLO WORLD"
key = random_key(np.random.randint(1, 27)).encode("utf-8")
encrypted = rc4_encrypt(plain, key).hex()
decrypted = rc4_encrypt(bytes.fromhex(encrypted), key)
print("RC4 Encrypt:", encrypted)
print("RC4 Decrypt:", decrypted)