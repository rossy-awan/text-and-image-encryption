# Image Encryption and FFT Compression

This repository contains two distinct functionalities related to image processing:

1. **Image Encryption and Decryption** using a key to apply a noise-based encryption and decryption algorithm.
2. **FFT (Fast Fourier Transform) Compression** that applies FFT to images, saves and loads FFT data using gzip compression, and reconstructs the image.

## Features

### 1. Image Encryption and Decryption

This script uses a basic encryption method that modifies the original image using random noise and an XOR operation with a generated key. The encrypted image can be decrypted back to the original image if the same key is provided.

#### Functions:
- `encrypt_image(image_path, encrypted_image_path, key)`: Encrypts an image by adding noise and applying an XOR operation using a randomly generated key.
- `decrypt_image(encrypted_image_path, decrypted_image_path, key)`: Decrypts the encrypted image by reversing the noise and XOR operation.

### 2. FFT Compression

This part of the repository uses the Fast Fourier Transform (FFT) to compress and decompress images. The script normalizes and compresses the FFT data into a gzip file format, which is then used to reconstruct the image.

#### Functions:
- `normalize_complex(data)`: Normalizes the real and imaginary parts of complex FFT data.
- `denormalize_complex(data, real_min, real_max, imag_min, imag_max)`: Denormalizes the FFT data back to the original range.
- `save_fft_to_gzip(f_data, filename)`: Saves the FFT data into a compressed gzip file.
- `load_fft_from_gzip(filename, shape)`: Loads the compressed FFT data from the gzip file and reconstructs it back to an image.

## Requirements

- Python 3.x
- NumPy
- OpenCV
- Gzip

You can install the required dependencies using:

```bash
pip install numpy opencv-python
```

## File Structure

- `encrypt_image()`: Encrypts an image using noise and XOR operation.
- `decrypt_image()`: Decrypts the encrypted image.
- `save_fft_to_gzip()`: Saves FFT data in compressed format.
- `load_fft_from_gzip()`: Loads FFT data from the compressed file.
- `image.jpg`: Example image file used for encryption and FFT compression.

## How to Use

### Encryption Example

1. Provide an image (e.g., `image.jpg`).
2. Run the script to encrypt the image and save the encrypted file as `encrypted_image.png`.
3. Decrypt the image using the same key, and the output will be saved as `decrypted_image.png`.

### FFT Compression Example

1. Provide an image (e.g., `image.jpg`).
2. The script will apply FFT to the image, normalize, and save the data in a compressed gzip file (`fft_data.txt.gz`).
3. The FFT data can then be loaded from the compressed file and used to reconstruct the original image.