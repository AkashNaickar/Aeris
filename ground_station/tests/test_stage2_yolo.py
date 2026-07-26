import numpy as np
from aeris.pipeline.stage2_micro import DISEASE_CLASSES


def test_disease_classes_non_empty():
    assert len(DISEASE_CLASSES) == 12


def test_healthy_in_classes():
    assert "Healthy" in DISEASE_CLASSES


def test_classify_returns_dict_on_empty_image():
    from aeris.pipeline.stage2_micro import classify_disease
    blank = np.zeros((640, 640, 3), dtype=np.uint8)
    result = classify_disease(blank)
    assert "disease" in result
    assert "confidence" in result
