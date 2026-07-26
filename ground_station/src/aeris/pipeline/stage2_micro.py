from pathlib import Path
import numpy as np
import cv2

from aeris.config import settings

DISEASE_CLASSES = [
    "Tomato_Early_Blight", "Tomato_Late_Blight", "Tomato_Leaf_Mold",
    "Tomato_Septoria", "Tomato_Spider_Mites", "Tomato_Target_Spot",
    "Tomato_Yellow_Leaf_Curl", "Potato_Early_Blight", "Potato_Late_Blight",
    "Rice_Leaf_Blast", "Rice_Brown_Spot", "Healthy",
]


def _load_model():
    try:
        from ultralytics import YOLO
        model_path = Path(settings.yolo_model_path)
        if model_path.suffix == ".onnx":
            return YOLO(str(model_path), task="detect")
        return YOLO(str(model_path))
    except Exception as e:
        print(f"[YOLO] Failed to load model: {e}")
        return None


_model = None


def classify_disease(image: np.ndarray) -> dict:
    global _model
    if _model is None:
        _model = _load_model()
    if _model is None:
        return {"disease": "Unknown", "confidence": 0.0, "bbox": None}

    results = _model(image, conf=settings.yolo_confidence, iou=settings.yolo_iou)
    result = results[0]

    if len(result.boxes) == 0:
        return {"disease": "Healthy", "confidence": 0.0, "bbox": None}

    box = result.boxes[0]
    cls_id = int(box.cls[0])
    confidence = float(box.conf[0])
    xyxy = box.xyxy[0].tolist()

    disease_name = DISEASE_CLASSES[cls_id] if cls_id < len(DISEASE_CLASSES) else "Unknown"

    return {
        "disease": disease_name,
        "confidence": round(confidence, 3),
        "bbox": [round(v, 1) for v in xyxy],
    }
