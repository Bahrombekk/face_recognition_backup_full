
# FaceID - Face Recognition System

**FaceID** is a face recognition system built on InsightFace, OpenCV, and LMDB technologies. This project is designed for real-time face detection, encoding, storage in a database, and recognition. The system offers high accuracy, fast performance, and flexibility, supporting both GPU and CPU modes.

## Key Features
- 📷 Collecting various face positions (straight, left, right, smile, light/dark) from a camera.
- 🔍 Encoding faces into 512-dimensional vectors (embeddings) using InsightFace.
- 💾 Storing and managing encodings efficiently with an LMDB database.
- 🎥 Real-time face recognition via a camera.
- 🛠 Support for both GPU and CPU (automatic detection).
- 📈 Testing and logging systems for monitoring processes.
- 📸 Comparing a given image with database entries.

## Structure
The project is organized into the following directories:
```
faceid/
├── data/                 # Data (images, datasets)
│   ├── dataset/          # Original face images
│   ├── aligned_dataset/  # Aligned (processed) images
│   └── temp/             # Temporary files
├── baza/                 # Database and backups
│   ├── face_encodings_db/ # LMDB database
│   ├── backups/          # Backup files
│   └── logs/             # Log files
├── cod/                  # Code files
│   ├── collector/        # Data collection
│   ├── config/           # Configurations
│   ├── encoder/          # Encoding and database management
│   ├── recognition/      # Recognition
│   ├── tests/            # Tests
│   ├── compare_image_with_database.py # Image comparison with database
│   └── main.py           # Main script
└── README.md             # This document
```

## Installation

### Requirements
- **Python**: Version 3.8 or higher.
- **Operating System**: Windows, Linux, or macOS.
- **Additional Libraries**:
  - OpenCV (`opencv-python>=4.5.5`)
  - NumPy (`numpy>=1.21`)
  - InsightFace (`insightface>=0.7`)
  - TensorFlow (`tensorflow>=2.10`)
  - LMDB (`lmdb>=1.3`)
  - Scikit-learn (`scikit-learn>=1.0`)
- **Optional for GPU**: NVIDIA CUDA 10.1+ and cuDNN.

### Installation Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Bahrombekk/face_recognition_backup_full.git
   cd faceid
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

3. **Install Required Packages**:
   Create a `requirements.txt` file with the following content:
   ```
   opencv-python>=4.5.5
   numpy>=1.21
   insightface>=0.7
   tensorflow>=2.10
   lmdb>=1.3
   scikit-learn>=1.0
   ```
   Then install the packages:
   ```bash
   pip install -r requirements.txt
   ```

4. **Load InsightFace Models**:
   The InsightFace models are automatically downloaded the first time the program runs. An internet connection is required.

---

## Usage

### Main Script
Use the `faceid/main.py` file to manage the project:
```bash
python faceid/main.py or python -m faceid.main
```

#### Options:
- **1. Collect User Face Data**:
  - Enter a user ID (e.g., `001`).
  - Show your face in various positions (straight, left, right, smile, light/dark) in front of the camera and press the `SPACE` key to confirm.

- **2. Encode Data**:
  - Automatically encodes images in the `aligned_dataset` folder and saves them to the LMDB database.

- **3. Add a New User**:
  - Enter a user ID and encode their images, adding them to the database.

- **4. Delete a User**:
  - Remove a user’s encodings from the database.

- **11. Start Real-Time Recognition**:
  - Begins real-time face detection and recognition via the camera. Press `q` to exit.

### Compare Image with Database
To compare a given image with database entries:
```bash
python faceid/compare_image_with_database.py
```
- Enter the image path (e.g., `/path/to/image.jpg`).
- The result will show the best match (if any) and the confidence level (0-100%).

---

## Configuration
You can modify the following settings in the `cod/config/config.py` file:
- `VIDEO_SOURCE`: Camera index (default: 2, try 0 for internal webcams).
- `MIN_CONFIDENCE`: Minimum confidence for face detection (default: 0.65).
- `ENCODING_TOLERANCE`: Similarity threshold for recognition (default: 0.6).
- `INSIGHTFACE_MODEL`: Model name to use (default: `buffalo_l`).

---

## Tests
To verify the system’s functionality, use the unittest framework:
```bash
python -m unittest discover faceid/tests
```
Tests are located in the `faceid/tests/` directory and include separate tests for each module.

---

## Important Notes
- **Camera Connection**: If the camera doesn’t work, change the `VIDEO_SOURCE` value or try different indices (0, 1, 2).
- **Logs**: Monitor processes by checking log files in the `baza/logs/` directory.
- **GPU Support**: If you have an NVIDIA GPU, install TensorFlow with CUDA support for faster performance.

---

## Authors
- **Bahrombek Muhammadiyev** - [GitHub Profile](https://github.com/Bahrombekk)
- Email: bahrombekmuhammadiyev@gmail.com

## License
This project is distributed under the MIT License. For more details, see the `LICENSE` file.

---

## Additional Information
- To extend the project or add new features, modify the modules in the `faceid/` directory.
- If you encounter any issues, report them via GitHub Issues or contact me directly.
- If you find this project useful, please star it on GitHub!

---
