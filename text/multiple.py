import random, string

# Algorithm
def vigenere_encrypt(text, key):
    res, k, ki = "", key.upper(), 0
    for ch in text.upper():
        if ch.isalpha():
            shift = ord(k[ki]) - 65
            res += chr((ord(ch)-65+shift)%26 + 65)
            ki = (ki + 1) % len(k)
        else: res += ch
    return res

def vigenere_decrypt(cipher, key):
    res, k, ki = "", key.upper(), 0
    for ch in cipher.upper():
        if ch.isalpha():
            shift = ord(k[ki]) - 65
            res += chr((ord(ch)-65-shift)%26 + 65)
            ki = (ki + 1) % len(k)
        else: res += ch
    return res

def caesar_encrypt(text, shift):
    out = ""
    for ch in text:
        if ch.isalpha():
            base = 65 if ch.isupper() else 97
            out += chr((ord(ch)-base+shift)%26 + base)
        else: out += ch
    return out

def caesar_decrypt(cipher, shift):
    return caesar_encrypt(cipher, -shift)

def substitution_encrypt(text, key):
    table = str.maketrans(string.ascii_uppercase, key)
    return text.upper().translate(table)

def substitution_decrypt(cipher, key):
    table = str.maketrans(key, string.ascii_uppercase)
    return cipher.upper().translate(table)

def transposition_encrypt(text, key):
    cols = [''] * key
    for i, ch in enumerate(text):
        cols[i % key] += ch
    return ''.join(cols)

def transposition_decrypt(cipher, key):
    n = len(cipher)
    col_len, extra = n // key, n % key
    cols, start = [], 0
    for i in range(key):
        end = start + col_len + (1 if i < extra else 0)
        cols.append(cipher[start:end]); start = end
    res = ''
    for i in range(max(len(c) for c in cols)):
        for c in cols:
            if i < len(c): res += c[i]
    return res

# Key helpers
def random_vigenere_key():
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(random.randint(3,8)))

def random_substitution_key():
    letters = list(string.ascii_uppercase)
    random.shuffle(letters)
    return ''.join(letters)

# Cascade
algos = ["CAESAR", "VIGENERE", "SUBSTITUTION", "TRANSPOSITION"]
def encrypt_file(input_file, output_file):
    plaintext = open(input_file, encoding="utf-8").read()
    order = algos[:]
    random.shuffle(order)
    caesar_k = random.randint(1, 25)
    trans_k = random.randint(2, 10)
    vig_k = random_vigenere_key()
    subs_k = random_substitution_key()
    text = plaintext
    for algo in order:
        if algo == "CAESAR":
            text = caesar_encrypt(text, caesar_k)
        elif algo == "VIGENERE":
            text = vigenere_encrypt(text, vig_k)
        elif algo == "SUBSTITUTION":
            text = substitution_encrypt(text, subs_k)
        elif algo == "TRANSPOSITION":
            text = transposition_encrypt(text, trans_k)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(text)
    key_string = f"{'>'.join(order)}!{caesar_k}#{trans_k}?{vig_k}@{subs_k}"
    print("KEY MASTER:\n", key_string)
    return key_string

def decrypt_file(input_file, output_file, key_string):
    data = open(input_file, encoding="utf-8").read()
    order_part, rest = key_string.split("!")
    order = order_part.split(">")
    caesar_k = int(rest.split("#")[0])
    trans_k = int(rest.split("#")[1].split("?")[0])
    vig_k = rest.split("?")[1].split("@")[0]
    subs_k = rest.split("@")[1]
    text = data
    for algo in reversed(order):
        if algo == "CAESAR":
            text = caesar_decrypt(text, caesar_k)
        elif algo == "VIGENERE":
            text = vigenere_decrypt(text, vig_k)
        elif algo == "SUBSTITUTION":
            text = substitution_decrypt(text, subs_k)
        elif algo == "TRANSPOSITION":
            text = transposition_decrypt(text, trans_k)
    open(output_file,"w",encoding="utf-8").write(text)

# Example
master_key = encrypt_file("decrypt.txt", "encrypt.txt")
decrypt_file("encrypt.txt", "decrypt.txt", master_key)