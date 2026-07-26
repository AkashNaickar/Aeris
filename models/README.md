# Models

| File | Format | Size | mAP@50 |
|------|--------|------|--------|
| `yolov8n_aeris.pt` | PyTorch | 6.2 MB | 0.89 |
| `yolov8n_aeris.onnx` | ONNX | 3.1 MB | 0.88 |

## Training

- Dataset: PlantVillage subset (12 classes)
- Epochs: 100
- Image size: 640×640
- Augmentation: mosaic, mixup, HSV jitter, flips

## Classes

Tomato_Early_Blight, Tomato_Late_Blight, Tomato_Leaf_Mold, Tomato_Septoria,
Tomato_Spider_Mites, Tomato_Target_Spot, Tomato_Yellow_Leaf_Curl,
Potato_Early_Blight, Potato_Late_Blight, Rice_Leaf_Blast, Rice_Brown_Spot,
Healthy

## Usage

```python
from ultralytics import YOLO
model = YOLO("models/yolov8n_aeris.onnx")
results = model("image.jpg")
```

**Note**: Actual model weights stored via Git LFS. Use `git lfs pull` to download.
