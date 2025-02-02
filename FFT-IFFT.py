import numpy as np
import cv2
import gzip

def normalize_complex(data):
    real_part = (np.real(data) - np.min(np.real(data))) / (np.max(np.real(data)) - np.min(np.real(data)))
    imag_part = (np.imag(data) - np.min(np.imag(data))) / (np.max(np.imag(data)) - np.min(np.imag(data)))
    return real_part + 1j * imag_part

def denormalize_complex(data, real_min, real_max, imag_min, imag_max):
    real_part = data.real * (real_max - real_min) + real_min
    imag_part = data.imag * (imag_max - imag_min) + imag_min
    return real_part + 1j * imag_part

def save_fft_to_gzip(f_data, filename, shape):
    f_data_normalized = normalize_complex(f_data) * scale_factor
    with gzip.open(filename, "wt") as f:
        f.write(f"{shape[0]},{shape[1]}\n")
        f.write(f"{np.min(np.real(f_data))},{np.max(np.real(f_data))},{np.min(np.imag(f_data))},{np.max(np.imag(f_data))}\n")
        np.savetxt(f, np.column_stack((np.real(f_data_normalized).flatten(), np.imag(f_data_normalized).flatten())), fmt="%d")

def load_fft_from_gzip(filename):
    with gzip.open(filename, "rt") as f:
        height, width = map(int, f.readline().strip().split(","))
        real_min, real_max, imag_min, imag_max = map(float, f.readline().strip().split(","))
        data = np.loadtxt(f, dtype=np.int32)
    real_part = data[:, 0].reshape((height, width))
    imag_part = data[:, 1].reshape((height, width))
    return denormalize_complex(real_part / scale_factor + 1j * imag_part / scale_factor, real_min, real_max, imag_min, imag_max)

scale_factor = 10**4
image_path = "image.jpg"
fft_compressed_txt_path = "fft_data.txt.gz"
recovered_image_path = "recovered_image.png"

image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
f_shifted = np.fft.fftshift(np.fft.fft2(image))
save_fft_to_gzip(f_shifted, fft_compressed_txt_path, image.shape)

f_reconstructed = load_fft_from_gzip(fft_compressed_txt_path)
restored_image = np.abs(np.fft.ifft2(np.fft.ifftshift(f_reconstructed)))
cv2.imwrite(recovered_image_path, restored_image.astype(np.uint8))