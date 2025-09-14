import numpy as np

def transposition_encrypt(text, key):
    columns = [''] * key
    for i, char in enumerate(text):
        columns[i % key] += char
    return ''.join(columns)

def transposition_decrypt(cipher, key):
    n = len(cipher)
    col_len = n // key
    extra = n % key
    columns = []
    start = 0
    for i in range(key):
        end = start + col_len + (1 if i < extra else 0)
        columns.append(cipher[start:end])
        start = end

    result = ''
    for i in range(max(len(col) for col in columns)):
        for col in columns:
            if i < len(col):
                result += col[i]
    return result

# Example
plain = "HELLO WORLD"
key = np.random.randint(0, 27)
encrypted = transposition_encrypt(plain, 4)
decrypted = transposition_decrypt(encrypted, 4)
print("Transposition Encrypt:", encrypted)
print("Transposition Decrypt:", decrypted)