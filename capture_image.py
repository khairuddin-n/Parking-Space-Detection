import os
import cv2
from IPython.display import Image, display

# Ambil nama file yang diunggah
video_file = 'parking3.mp4'
camera = cv2.VideoCapture(video_file)

# Baca frame pertama
ret, frame = camera.read()

if ret:
    print("Frame pertama dari video berhasil dibaca.")
    # Simpan frame pertama sebagai gambar
    img_name = "tempat_parkir_3.png"
    print(f"Menyimpan frame pertama sebagai '{img_name}' ...")
    cv2.imwrite(img_name, frame)
    print(f"Frame pertama berhasil disimpan sebagai '{img_name}'.")
else:
    print("Tidak dapat membaca frame pertama dari video.")

camera.release()