from ultralytics import YOLO

model = YOLO("yolov8n-seg.pt")

model.train(
    data="coco8.yaml",   # 🔥 CHANGE THIS (not coco8-seg.yaml)
    epochs=5,
    imgsz=640
)