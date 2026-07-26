# Dataset: PlantVillage Subset

We use a curated subset of the [PlantVillage dataset](https://www.kaggle.com/datasets/emmarex/plantdisease) for YOLOv8 training.

## Classes (12)

| Crop      | Diseases                            |
|-----------|-------------------------------------|
| Tomato    | Early Blight, Late Blight, Leaf Mold, Septoria, Spider Mites, Target Spot, Yellow Leaf Curl |
| Potato    | Early Blight, Late Blight           |
| Rice      | Leaf Blast, Brown Spot              |
| Healthy   | All crops                           |

## Preprocessing

- Resize: 640×640 (YOLOv8 default)
- Augmentation: mosaic, mixup, HSV jitter, flips (via Roboflow)
- Split: 80/10/10 train/val/test

## Usage

```python
# Download via Roboflow
from roboflow import Roboflow
rf = Roboflow(api_key="your_key")
project = rf.workspace("aeris").project("plantvillage-subset")
dataset = project.version(1).download("yolov8")
```

**Note**: Actual image files are stored externally. See `data/plantvillage_subset/.gitkeep`.
