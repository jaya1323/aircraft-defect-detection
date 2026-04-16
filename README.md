# Aircraft Defect Detection using YOLOv8

## Overview
This project focuses on building an AI-powered computer vision system to automatically detect aircraft surface defects using YOLOv8. The system identifies structural anomalies such as cracks, corrosion, and surface irregularities from inspection images.

Traditional aircraft inspection is time-consuming and manual. This project demonstrates how deep learning can automate inspection, improve consistency, and reduce human effort.

---

## Key Features
- Automated detection of aircraft surface defects  
- Real-time inference (~14–20 ms per image)  
- End-to-end machine learning pipeline  
- Bounding box detection for defect localization  
- Trained on custom annotated dataset  

---

## Tech Stack
- Python  
- PyTorch  
- YOLOv8 (Ultralytics)  
- OpenCV  
- NumPy  

---

## Project Structure
aircraft-defect-detection/
│
├── convert.py          # XML to YOLO conversion  
├── split_data.py       # Train-validation split  
├── dataset.yaml        # Dataset config  
├── best.pt             # Trained model  
├── README.md  

---

## Workflow Pipeline
1. Data Collection  
2. Annotation (XML format)  
3. Conversion to YOLO format  
4. Dataset splitting  
5. Model training (YOLOv8)  
6. Evaluation and prediction  

---

## Model Performance
- mAP50: ~0.49  
- Precision: ~0.60  
- Recall: ~0.47  
- Inference Speed: ~14 ms/image  

---

## How to Run

### Install dependencies
pip install ultralytics  

### Train model
yolo detect train data=dataset.yaml model=yolov8n.pt epochs=30 imgsz=640  

### Run prediction
yolo detect predict model=best.pt source=images/  

---

## 📸 Results
The model detects defects and highlights them with bounding boxes.

(Add screenshots here)

---

## Applications
- Aircraft maintenance inspection  
- Surface defect detection  
- Industrial quality inspection  
- Automated inspection systems  

---

## Future Improvements
- Train with larger dataset  
- Use YOLOv8m for better accuracy  
- Deploy as web app  
- Real-time detection using camera  

---

## Impact
- Reduces manual inspection effort  
- Improves detection consistency  
- Enables scalable inspection systems  

---

## Author
Kalla Jayasree  
Aerospace Engineering | AI/ML Enthusiast  

---

## ⭐ Acknowledgements
- Ultralytics YOLOv8  
- Open-source community  
