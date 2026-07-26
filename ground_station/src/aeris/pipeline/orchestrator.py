import time
from pathlib import Path
import cv2
import numpy as np

from aeris.config import settings
from aeris.ingest.exif_parser import parse_gps, parse_gps_from_filename
from aeris.pipeline.stage1_macro import detect_stress_zones
from aeris.pipeline.stage2_micro import classify_disease
from aeris.pipeline.stage3_forecast import compute_risk_score


def run_pipeline(image_path: str | Path) -> dict:
    image_path = Path(image_path)
    img = cv2.imread(str(image_path))
    if img is None:
        raise FileNotFoundError(f"Cannot read image: {image_path}")

    result = {
        "image": image_path.name,
        "timestamp": time.time(),
        "gps": None,
    }

    gps = parse_gps(image_path)
    if gps is None:
        gps = parse_gps_from_filename(image_path.stem)
    result["gps"] = gps

    use_ndvi = "nir" in image_path.stem.lower() or "noir" in image_path.stem.lower()
    stage1 = detect_stress_zones(img, use_ndvi=use_ndvi)
    result["stage1"] = stage1

    stage2 = classify_disease(img)
    result["stage2"] = stage2

    stage3 = compute_risk_score(
        disease=stage2["disease"],
        confidence=stage2["confidence"],
    )
    result["stage3"] = stage3

    return result


def format_result(result: dict) -> str:
    gps_str = f"({result['gps'][0]:.6f}, {result['gps'][1]:.6f})" if result["gps"] else "N/A"
    return (
        f"[Aeris] {result['image']}\n"
        f"  GPS: {gps_str}\n"
        f"  Stage 1 (Stress): {'STRESSED' if result['stage1']['stressed'] else 'HEALTHY'}\n"
        f"  Stage 2 (Disease): {result['stage2']['disease']} ({result['stage2']['confidence']:.1%})\n"
        f"  Stage 3 (Risk): {result['stage3']['risk_level']} ({result['stage3']['risk_score']:.2f})"
    )
