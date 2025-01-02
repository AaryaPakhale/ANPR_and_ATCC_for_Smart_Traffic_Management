# ANPR and ATCC for Smart Traffic Management

Welcome to the GitHub repository for our cutting-edge solution for modern traffic management! This project leverages Automatic Number Plate Recognition (ANPR) and Automatic Traffic Classification and Control (ATCC) to optimize traffic systems in smart city environments. By combining advanced technologies and data-driven approaches, we aim to enhance efficiency, reduce congestion, and pave the way for smarter urban mobility. Dive into the repository to explore innovative tools, algorithms, and implementations that contribute to this transformative initiative!

## Table of Contents

- [ Project Overview](#-project-overview)
- [Key Features](#key-features)
- [Technologies Used](#technologies-used)
- [Results](#results)
- [Project Structure](#%EF%B8%8F-project-structure)
- [Workflow](#-workflow)
- [Setup and Installation](#%EF%B8%8F-setup-and-installation)
- [Running the Project](#%EF%B8%8F-running-the-project)
- [License](#-license)

---

## 🎯 Project Overview
We implement an intelligent traffic management system utilizing Automatic Number Plate Recognition (ANPR) and Automatic Traffic Classification and Control (ATCC). By leveraging Deep Learning and Object Detection techniques, this system automates traffic monitoring and control in smart city environments.

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
- You can file the result videos at these locations : [Video-1](https://drive.google.com/file/d/1z7LEhVbaaN2FSX3jxYZvDRm6PXXoRTGL/view?usp=sharing)
                                                   [Video-2](https://drive.google.com/file/d/1IvPMZraIPtYgs1NVtuqPxiFVSoWfwiUL/view?usp=sharing)

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


