import cv2
import numpy as np

# Mengatur nama file gambar parkir dan file koordinat
image_file = "tempat_parkir_3.png"
coord_file = "koordinat_3.txt"

# Memuat gambar parkir
image = cv2.imread(image_file)

if image is None:
    raise ValueError("Gambar tidak ditemukan atau tidak bisa dibuka.")

# Mengosongkan file koordinat
with open(coord_file, "w") as file:
    pass

# Daftar untuk menyimpan titik koordinat
parking_coordinates = []

# Fungsi callback mouse untuk mendapatkan koordinat pada klik mouse
def get_parking_coordinates(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        parking_coordinates.append((x, y))
        print(f"Koordinat: ({x}, {y})")

# Menampilkan gambar dan menangani event mouse
cv2.namedWindow("Area Parkir")
cv2.setMouseCallback("Area Parkir", get_parking_coordinates)

while True:
    image_resized = cv2.resize(image, (1300, 650), interpolation=cv2.INTER_AREA)

    # Gambar koordinat parkir yang ada
    for coord in parking_coordinates:
        cv2.circle(image_resized, coord, 5, (0, 0, 255), -1)

    # Gambar garis untuk membentuk area parkir setiap 4 titik
    for i in range(0, len(parking_coordinates), 4):
        if i + 3 < len(parking_coordinates):
            cv2.polylines(image_resized, [np.array(parking_coordinates[i:i+4], np.int32)], True, (0, 255, 0), 2)

    cv2.imshow("Area Parkir", image_resized)
    key = cv2.waitKey(1) & 0xFF

    if key == 27:  # Tekan 'Esc' untuk keluar
        break

cv2.destroyAllWindows()

# Restrukturisasi koordinat ke dalam grup berisi 4
parking_areas = [parking_coordinates[i:i + 4] for i in range(0, len(parking_coordinates), 4)]

# Simpan koordinat ke dalam file
with open(coord_file, "w") as f:
    for area in parking_areas:
        for point in area:
            f.write(f"{point[0]} {point[1]} ")
        f.write("\n")

print(f"Koordinat parkir disimpan di '{coord_file}'")
