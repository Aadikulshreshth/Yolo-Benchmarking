from ultralytics import YOLO
import csv

models = [
    "yolov8n.pt",
    "yolov8s.pt",
    "yolov8m.pt",
    "yolo11n.pt",
    "yolo11s.pt"
]

thresholds = [0.25, 0.50, 0.75]

with open("threshold_results.csv", "w", newline="") as f:

    writer = csv.writer(f)
    writer.writerow([
        "Model",
        "Confidence",
        "Precision",
        "Recall",
        "mAP50",
        "mAP50-95"
    ])

    for model_name in models:

        model = YOLO(model_name)

        for conf in thresholds:

            print(f"\n{model_name}  |  conf={conf}")

            metrics = model.val(
                data=r"C:\Users\AADI\Yolo\benchmark_coco\dataset.yaml",
                imgsz=640,
                device=0,
                workers=0,
                conf=conf
            )

            writer.writerow([
                model_name,
                conf,
                metrics.box.mp,
                metrics.box.mr,
                metrics.box.map50,
                metrics.box.map
            ])