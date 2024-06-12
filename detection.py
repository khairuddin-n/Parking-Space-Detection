import numpy as np
import cv2
from ultralytics import YOLO
from IPython.display import display, Image

camera = cv2.VideoCapture("parking1.mp4")

model = YOLO('datasets/runs/detect/train/weights/best.pt')

file = open("koordinat_1.txt")

print("Loading parking coordinates ...")

lines = file.readlines()

lines = [line.strip() for line in lines]

total_parking_lots = len(lines)

parking_lot_coords = list()

for i in range(len(lines)):
    coords = lines[i].split()
    top_left = (int(coords[0]), int(coords[1]))
    top_right = (int(coords[2]), int(coords[3]))
    bottom_right = (int(coords[4]), int(coords[5]))
    bottom_left = (int(coords[6]), int(coords[7]))
    coord = np.array([top_left,top_right, bottom_right,bottom_left])
    parking_lot_coords.append(coord)

paused = False  

while True:
    available_slot = len(parking_lot_coords)
    
    if not paused:
        ret, frame = camera.read()

        if not ret:
            print("Failed to initialize camera.")
            cv2.destroyAllWindows()
            break

        frame = cv2.resize(frame, (1300, 650))
        for i in range(len(parking_lot_coords)):
            cv2.polylines(frame, [np.array(parking_lot_coords[i], np.int32)], True, (0, 255, 0), 2)
            
        results = model.predict(frame)
        result = results[0]

        for box in result.boxes:
            class_id = box.cls[0].item()
            if class_id == 0.0:
                cord = box.xyxy[0].tolist()
                cord = [round(x) for x in cord]
                cx = int(cord[0] + cord[2]) // 2
                cy = int(cord[1] + cord[3]) // 2
                point = (cx, cy)
                
                for arr in parking_lot_coords:
                    if cv2.pointPolygonTest(np.array(arr, np.int32), ((cx, cy)), False) >= 0:
                        available_slot -= 1   
                        cv2.polylines(frame, [np.array(arr, np.int32)], True, (0, 0, 255), 2)
                        
        print(available_slot)
        cv2.putText(frame, "Available Slots: " + str(available_slot), (50, 25), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)   

        cv2.imshow("Camera", frame)

    # Tangani input keyboard
    key = cv2.waitKey(30)

    if key % 256 == 27:
        # Tekan 'ESC' untuk keluar
        print("Camera terminated.")
        cv2.destroyAllWindows()
        break
    elif key % 256 == 32:
        # Tekan 'Space' untuk menjeda atau melanjutkan video
        paused = not paused
        if paused:
            print("Video paused.")
        else:
            print("Video resumed.")

