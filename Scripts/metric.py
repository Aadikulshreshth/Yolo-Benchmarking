from ultralytics import YOLO

def main():

    models = [
        "yolov8n.pt",
        "yolov8s.pt",
        "yolov8m.pt",
        "yolo11n.pt",
        "yolo11s.pt"
    ]

    for model_name in models:

        print(f"\nEvaluating {model_name}")

        model = YOLO(model_name)

        metrics = model.val(
            data=r"\dataset.yaml",
            split="val",
            device=0,
            imgsz=640
        )

        print("Precision:", metrics.box.mp)
        print("Recall:", metrics.box.mr)
        print("mAP50:", metrics.box.map50)
        print("mAP50-95:", metrics.box.map)

if __name__ == "__main__":
    main()
