from ultralytics import YOLO
import time
import os
import pandas as pd
import torch

MODELS = [
    "yolov8n.pt",
    "yolov8s.pt",
    "yolov8m.pt",
    "yolo11n.pt",
    "yolo11s.pt"
]

results = []

for model_path in MODELS:

    print(f"\nRunning {model_path}")

    model = YOLO(model_path)

    torch.cuda.empty_cache()

    start = time.time()

    model.predict(
        source=r"C:\Users\AADI\Yolo\benchmark\images",
        device=0,
        save=False,
        verbose=False
    )

    end = time.time()

    total_time = end - start

    size_mb = os.path.getsize(model_path) / (1024 * 1024)

    fps = 2000 / total_time

    results.append({
        "Model": model_path,
        "Size_MB": round(size_mb, 2),
        "Total_Time_s": round(total_time, 2),
        "FPS": round(fps, 2)
    })

df = pd.DataFrame(results)

print(df)

df.to_csv("benchmark_results.csv", index=False)

print("\nSaved benchmark_results.csv")