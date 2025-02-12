## Simple Computer Vision Project: Parking Spot Detection and YOLO Training  

### Project Overview  
This repository contains a simple computer vision project that demonstrates several functionalities related to parking spot detection using YOLO. The project consists of scripts for:
- Capturing an Image: Extracting the first frame from a video.
- Annotating Coordinates: Manually selecting parking area coordinates on an image.
- Vehicle Detection: Detecting vehicles in a parking video and determining available parking spots based on pre-defined coordinates.
- Model Training: Training a YOLO model for car detection using a Jupyter Notebook and the Roboflow API.

### Repository Structure  
```
.
├── capture_image.py      # Extracts the first frame from a video (parking3.mp4) and saves it as an image.
├── coordinates.py        # Provides an interface to annotate parking area coordinates on the extracted image.
├── detection.py          # Performs vehicle detection on a parking video (parking1.mp4) and highlights available parking spots.
├── model_train.ipynb     # Jupyter Notebook for training a YOLO model using the Roboflow API.
├── requirements.txt      # Lists the required Python packages.
├── koordinat_1.txt       # Example coordinate file for parking areas.
├── parking1.mp4          # Sample parking video used for detection.
├── tempat_parkir_1.png   # Example parking area image.
└── (other related files)
```

### Detailed Description  
1. `capture_image.py`
   - Purpose: Opens a video file (`parking1.mp4`), extracts the first frame, and saves it as `tempat_parkir_1.png`.
   - Usage: Run the script with Python. It will read the video file, capture the first frame, and save the image automatically.
2. `coordinates.py`
   - Purpose: Allows the user to annotate parking area coordinates on the image (`tempat_parkir_1.png`).
   - Functionality:
     - Opens the image in a window.
     - On mouse left-click, records the coordinate points.
     - Groups every 4 points into a parking area.
     - Saves the coordinates into `koordinat_1.txt`.
   - Usage: Run the script, click on the image to mark points, and press `Esc` to exit and save the coordinates.
3. `detection.py`
    - Purpose: Detects vehicles in a parking video (`parking1.mp4`) using a YOLO model, and checks for available parking spots based on coordinates defined in `koordinat_1.txt`.
    - Functionality:
      - Loads a YOLO model (using weights from `datasets/runs/detect/train/weights/best.pt`).
      - Reads parking area coordinates from a coordinate file.
      - Processes video frames to detect vehicles.
      - Uses the detected vehicle positions to mark occupied spots and updates the count of available parking slots.
      - Displays the frame with the detection results and available slot count.
      - Supports pausing/resuming the video with the `Space` key and exiting with the `Esc` key.
    - Usage: Run the script ensuring all required files (video, coordinate file, model weights) are in place.
4. `model_train.ipynb`
     - Purpose: A Jupyter Notebook that demonstrates how to train a YOLO model for car detection.
     - Functionality:
       - Uses the Roboflow API to download a dataset.
       - Configures training parameters such as epochs, batch size, and image size.
       - Trains the YOLO model and evaluates its performance.
     - Usage:
       - Open the notebook in Jupyter Notebook and execute the cells sequentially.
       - Ensure you have created a `.env` file with your Roboflow API key for authentication.  

  ### Requirements  
  Make sure to install the required packages before running any of the scripts. You can install the dependencies by running:
  ```
  pip install -r requirements.txt
  ```

### Setup Instructions  
  1. Clone the Repository:
     ```
     git clone https://github.com/khairuddin-n/Parking-Space-Detection.git
     cd Parking-Space-Detection
     ```
  2. Install Dependencies:
     ```
     pip install -r requirements.txt
     ```
  3. Additional Files:
     - Ensure you have the necessary files (`koordinat_1.txt`, `parking1.mp4`, `tempat_parkir_1.png`, etc.) in the repository.
     - Verify that file names and paths match those expected by the scripts. If needed, update the paths in the code accordingly.
   4. Configure Environment Variables (for Model Training):
      - Create a .env file in the root directory with your Roboflow API key:
        ```
        API_KEY=your_roboflow_api_key
        ```
 ### Running the Project   
 - **Train the YOLO Model**:  
   Open the `model_train.ipynb` notebook in Jupyter Notebook and run the cells to download the dataset, train the model, and evaluate its performance.    
 - **Capture Image**:  
   Run the following command to extract and save the first frame of the video:
   ```
   python capture_image.py
   ```
 - **Annotate Coordinates**:  
   Run the script to annotate parking area coordinates on the saved image:
   ```
   python coordinates.py
   ```
 - **Run Detection**:  
   To detect vehicles and determine available parking spots, run:
   ```
   python detection.py
   ```  
