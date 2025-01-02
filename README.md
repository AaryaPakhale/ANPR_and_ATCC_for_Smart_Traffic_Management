# ANPR and ATCC for Smart Traffic Management

Welcome to the ANPR and ATCC for Smart Traffic Management repository! This project aims to revolutionize traffic management in smart city environments by utilizing advanced technologies like Automatic Number Plate Recognition (ANPR) and Automatic Traffic Classification and Control (ATCC).

## Table of Contents

- [ Project Overview](#introduction)
- [Key Features](#project-structure)
- [Technologies Used]
- [Results](#features)
- [Project Structure](#technologies-used)
- [Workflow](#setup-instructions)
- [Setup and Installation](#usage)
- [Running the Project](#output)
- [License](#license)

---

## 🎯 Project Overview
This project implements an intelligent traffic management system utilizing Automatic Number Plate Recognition (ANPR) and Automatic Traffic Classification and Control (ATCC). By leveraging Deep Learning and Object Detection techniques, the system automates traffic monitoring and control in smart city environments.

### Key Features
- 📝 Automatic Number Plate Recognition (ANPR)
- 🚦 Automatic Traffic Classification and Control (ATCC)
- 📊 Data interpolation for accurate tracking
- 📈 Visualization capabilities

### Technologies Used
- **Programming Language**: Python
- **Libraries**: listed in `requirements.txt`
- **Deep Learning**: Object detection models (e.g., YOLO)

### Results
- You can file the result video at this location : [Link-1](https://drive.google.com/file/d/1z7LEhVbaaN2FSX3jxYZvDRm6PXXoRTGL/view?usp=sharing)
                                                   [Link-2](https://drive.google.com/file/d/1IvPMZraIPtYgs1NVtuqPxiFVSoWfwiUL/view?usp=sharing)

## 🏗️ Project Structure
```
ANPR_and_ATCC_for_Smart_Traffic_Management/
├── .idea/
├── CV_Basics/                      # Computer vision and OCR learning materials
├── Image_processing/               # Image processing for clearer detections
├── Interpolation/                  # Data interpolation script
├── Testing/                        # Project testing files
├── Video_processing/               # Visualizing and video processing files
├── YOLO_training/                  # Fine-tuning YOLO for license plate detection
├── interpolated_results/           # Interpolated CSV files for visualization
├── object_tracker/                 # Main detection and vehicle tracking code
├── results/                        # Initial detection CSV files
├── utils/                          # Code for OCR corrections
├── .gitignore                      # Git ignore rules
├── main.py                         # Main execution file
└── requirements.txt                # Library installations

```

## 🚀 Workflow
1. Execute `main.py` to perform initial vehicle detection and generate CSV file in `results/` directory
2. Run `Interpolation/add_missing_data.py` to perform data interpolation and generate enhanced CSV file in `interpolated_results/` directory
3. Run `Video_processing/visualize.py` to create visualization video using interpolated data, saved in `output_videos/` directory

## 🛠️ Setup and Installation
1. Clone the repository:
```bash
git clone https://github.com/AaryaPakhale/ANPR_and_ATCC_for_Smart_Traffic_Management
cd ANPR_and_ATCC_for_Smart_Traffic_Management
```

2. Create and activate conda environment (recommended):
```bash
conda create --name stm 
conda activate stm
```
Note: Can be done using virtual environment also
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables (If using virtual environment):
- Create a copy of `.env.example` (if provided) and rename it to `.env`
- Update the necessary secret keys and configurations

## 🏃‍♂️ Running the Project


1. Replace the path to your input video and your desired output directory.

2. Run the main detection:
```bash
python main.py
```

3. Perform data interpolation:
```bash
python add_missing_data.py
```

4. Generate visualization:
```bash
python visualize.py
```

## 📄 License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/AaryaPakhale/ANPR_and_ATCC_for_Smart_Traffic_Management/blob/main/LICENSE) file for details.


