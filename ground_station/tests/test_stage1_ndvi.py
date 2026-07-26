import numpy as np
import cv2
from aeris.pipeline.stage1_macro import compute_ndvi, compute_vari, detect_stress_zones


def test_ndvi_healthy_returns_false():
    green_img = np.full((100, 100, 3), (0, 255, 0), dtype=np.uint8)
    _, stressed = compute_ndvi(green_img)
    assert stressed is False


def test_ndvi_stressed_returns_true():
    brown_img = np.full((100, 100, 3), (100, 80, 60), dtype=np.uint8)
    _, stressed = compute_ndvi(brown_img)
    assert stressed is True


def test_vari_healthy_returns_false():
    green_img = np.full((100, 100, 3), (0, 255, 0), dtype=np.uint8)
    _, stressed = compute_vari(green_img)
    assert stressed is False


def test_detect_stress_zones_returns_dict():
    img = np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8)
    result = detect_stress_zones(img, use_ndvi=True)
    assert "stressed" in result
    assert "stress_pct" in result
