import os, struct

def pad(data: bytes) -> bytes:
    pad_len = 8 - (len(data) % 8)
    return data + bytes([pad_len]) * pad_len

def unpad(data: bytes) -> bytes:
    pad_len = data[-1]
    return data[:-pad_len]

def tea_encrypt_block(v: bytes, k: bytes) -> bytes:
    v0, v1 = struct.unpack('>2I', v)
    k0, k1, k2, k3 = struct.unpack('>4I', k)
    delta = 0x9E3779B9
    s = 0
    for _ in range(32):
        s = (s + delta) & 0xFFFFFFFF
        v0 = (v0 + (((v1 << 4) + k0) ^ (v1 + s) ^ ((v1 >> 5) + k1))) & 0xFFFFFFFF
        v1 = (v1 + (((v0 << 4) + k2) ^ (v0 + s) ^ ((v0 >> 5) + k3))) & 0xFFFFFFFF
    return struct.pack('>2I', v0, v1)

def tea_decrypt_block(v: bytes, k: bytes) -> bytes:
    v0, v1 = struct.unpack('>2I', v)
    k0, k1, k2, k3 = struct.unpack('>4I', k)
    delta = 0x9E3779B9
    s = (delta * 32) & 0xFFFFFFFF
    for _ in range(32):
        v1 = (v1 - (((v0 << 4) + k2) ^ (v0 + s) ^ ((v0 >> 5) + k3))) & 0xFFFFFFFF
        v0 = (v0 - (((v1 << 4) + k0) ^ (v1 + s) ^ ((v1 >> 5) + k1))) & 0xFFFFFFFF
        s = (s - delta) & 0xFFFFFFFF
    return struct.pack('>2I', v0, v1)

def tea_encrypt(data: bytes, key: bytes) -> bytes:
    data = pad(data)
    blocks = [data[i:i+8] for i in range(0, len(data), 8)]
    return b"".join(tea_encrypt_block(b, key) for b in blocks)

def tea_decrypt(data: bytes, key: bytes) -> bytes:
    blocks = [data[i:i+8] for i in range(0, len(data), 8)]
    plain = b"".join(tea_decrypt_block(b, key) for b in blocks)
    return unpad(plain)

# Example
plain = b"HELLO WORLD"
key = os.urandom(16)
enc = tea_encrypt(plain, key)
encrypted = tea_encrypt(plain, key).hex()
decrypted = tea_decrypt(bytes.fromhex(encrypted), key)
print("TEA Encrypt:", encrypted)
print("TEA Decrypt:", decrypted)