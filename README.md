# Classical Ciphers and Image Encryption

This repository contains implementations of classical cryptography algorithms for **text** and simple encryption methods for **images** (PNG/JPG). Experiments include Caesar, Vigenère, Substitution, Transposition, XOR, RC4, TEA, as well as image encryption using XOR and RC4.

## Features

### Classical Text Ciphers

Various classical cryptographic algorithms implemented in Python:

| Algorithm | Description |
|-----------|-------------|
| **Caesar Cipher** | Shifts letters by a simple numeric key. |
| **Vigenère Cipher** | Uses a keyword to shift letters. |
| **Substitution Cipher** | Maps the alphabet to another alphabet randomly. |
| **Transposition Cipher** | Rearranges the order of characters in a message. |
| **XOR Cipher** | Performs a byte-by-byte XOR operation with a key. |
| **RC4 Stream Cipher** | A symmetric stream cipher for encrypting data. |
| **TEA (Tiny Encryption Algorithm)** | A lightweight block cipher using arithmetic operations. |

### Image Encryption (PNG/JPG)

#### XOR Image Encryption
This method adds **random noise** and applies an XOR operation to each pixel.
- `encrypt_image(image_path, encrypted_image_path, key)`
- `decrypt_image(encrypted_image_path, decrypted_image_path, key)`

> Use `.png` to preserve exact pixel values.

#### RC4 File Encryption
RC4 is used to encrypt the entire image file at the byte-stream level.
- `rc4_encrypt_file(image_path, encrypted_path, key)`
- `rc4_decrypt_file(encrypted_path, decrypted_path, key)`

> The encrypted result is not viewable as an image. Save it as `.enc` or `.bin`.

## Requirements
- Python 3.x  
- `numpy`  
- `opencv-python`

Install dependencies:

```bash
pip install numpy opencv-python
```

## Notes
- **JPG** uses lossy compression, so pixel-based encryption (like XOR) should use **PNG** for perfect recovery.  
- RC4 and TEA are symmetric: the same key is used for both encryption and decryption.  
- These implementations are for educational purposes — do not use them for production security.