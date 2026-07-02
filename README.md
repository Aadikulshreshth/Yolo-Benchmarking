# 📊 YOLO Benchmarking and Comparative Analysis

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![PyTorch](https://img.shields.io/badge/PyTorch-2.11-red?logo=pytorch)
![Ultralytics](https://img.shields.io/badge/Ultralytics-YOLO-purple)
![CUDA](https://img.shields.io/badge/CUDA-12.8-green?logo=nvidia)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-blue?logo=opencv)
![Status](https://img.shields.io/badge/Status-Completed-success)
![License](https://img.shields.io/badge/License-MIT-yellow)

A benchmarking framework developed during my internship to evaluate and compare multiple pretrained **YOLO** object detection models using a custom benchmark dataset.

The project focuses on comparing **computational performance**, **detection accuracy**, and the effect of different **confidence thresholds** under identical experimental conditions.

---

# 📌 Features

- Benchmarking multiple pretrained YOLO models
- Custom benchmark dataset creation
- Annotation conversion to YOLO format
- GPU accelerated inference using CUDA
- Confidence threshold analysis
- CSV based result generation
- Performance visualization

---

# 🤖 Models Evaluated

| Model | Type |
|--------|------|
| YOLOv8n | Nano |
| YOLOv8s | Small |
| YOLOv8m | Medium |
| YOLO11n | Nano |
| YOLO11s | Small |

---

# 📂 Dataset

The benchmark dataset was created using images collected from:

- **BDD100K**
- **Cityscapes**

Dataset Statistics

| Description | Count |
|------------|------:|
| Total Images | 2000 |
| Labeled Images | 1500 |
| Background Images | 500 |

Object Classes

- Person
- Car
- Bus
- Motorcycle
- Bicycle

> **Note**
>
> The benchmark dataset is **not included** in this repository due to its large size and licensing restrictions.
>
> You can download the original datasets from:
>
> - https://bdd-data.berkeley.edu/
> - https://www.cityscapes-dataset.com/

---

# 📊 Evaluation Metrics

### Computational Metrics

- Model Size
- Total Processing Time
- Average Inference Time
- FPS

### Detection Metrics

- Precision
- Recall
- mAP@50
- mAP@50-95

---

# 📈 Benchmark Results

## Computational Performance

| Model | Size (MB) | Total Time (s) | FPS |
|--------|----------:|---------------:|----:|
| YOLOv8n | 6.25 | 43.35 | 46.14 |
| YOLOv8s | 21.54 | **41.92** | **47.72** |
| YOLOv8m | 49.72 | 44.50 | 44.94 |
| YOLO11n | **5.35** | 42.65 | 46.89 |
| YOLO11s | 18.42 | 44.00 | 45.46 |

## Detection Performance

| Model | Precision | Recall | mAP@50 | mAP@50-95 |
|--------|----------:|-------:|--------:|----------:|
| YOLOv8n | 0.1020 | 0.0945 | 0.0393 | 0.0181 |
| YOLOv8s | 0.1110 | 0.1073 | 0.0492 | 0.0235 |
| YOLOv8m | **0.1171** | **0.1290** | **0.0572** | **0.0273** |
| YOLO11n | 0.1060 | 0.1001 | 0.0401 | 0.0183 |
| YOLO11s | 0.1159 | 0.1153 | 0.0512 | 0.0242 |

---

# 🗂️ Project Structure

```
YOLO-Benchmarking/
│
├── scripts/
├── results/
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/<username>/YOLO-Benchmarking.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 📁 Repository Contents

- Benchmarking scripts
- Evaluation scripts
- Performance results
- Threshold analysis
- Internship report
- Sample outputs

---

# 🔮 Future Improvements

- Fine-tune YOLO models on the benchmark dataset
- Benchmark newer YOLO versions
- Evaluate additional object detection architectures
- Deploy on edge devices
- Expand the benchmark dataset

---

# 📚 References

- Ultralytics YOLO Documentation
- PyTorch Documentation
- BDD100K Dataset
- Cityscapes Dataset

---

# 📄 License

This project is released for educational and research purposes.
