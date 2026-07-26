import numpy as np
import cv2

from aeris.config import settings


def compute_ndvi(nir_img: np.ndarray) -> tuple[np.ndarray, bool]:
    b, g, r = cv2.split(nir_img)
    nir = r.astype(np.float32)
    red = b.astype(np.float32)
    denominator = nir + red + 1e-10
    ndvi = (nir - red) / denominator
    mean_ndvi = float(np.mean(ndvi))
    stressed = mean_ndvi < settings.ndvi_threshold
    return ndvi, stressed


def compute_vari(rgb_img: np.ndarray) -> tuple[np.ndarray, bool]:
    b, g, r = cv2.split(rgb_img.astype(np.float32))
    denominator = r + g - b + 1e-10
    vari = (g - r) / denominator
    mean_vari = float(np.mean(vari))
    stressed = mean_vari < settings.vari_threshold
    return vari, stressed


def detect_stress_zones(image: np.ndarray, use_ndvi: bool = True) -> dict:
    mask = np.ones((image.shape[0] // 32, image.shape[1] // 32), dtype=bool)
    if use_ndvi:
        _, stressed = compute_ndvi(image)
    else:
        _, stressed = compute_vari(image)
    return {
        "stressed": stressed,
        "stress_pct": float(np.mean(mask)) * 100 if stressed else 0.0,
    }
