from pathlib import Path
import piexif
import numpy as np
import cv2


def parse_gps(image_path: str | Path) -> tuple[float, float] | None:
    img = cv2.imread(str(image_path))
    if img is None:
        return None
    try:
        exif_dict = piexif.load(str(image_path))
        gps = exif_dict.get("GPS", {})
        if not gps:
            return None
        lat = _dms_to_decimal(gps.get(piexif.GPSIFD.GPSLatitude))
        lon = _dms_to_decimal(gps.get(piexif.GPSIFD.GPSLongitude))
        lat_ref = gps.get(piexif.GPSIFD.GPSLatitudeRef, b"N")
        lon_ref = gps.get(piexif.GPSIFD.GPSLongitudeRef, b"E")
        if lat is not None and lon is not None:
            if lat_ref == b"S":
                lat = -lat
            if lon_ref == b"W":
                lon = -lon
            return (lat, lon)
    except Exception:
        return None
    return None


def parse_gps_from_filename(filename: str) -> tuple[float, float] | None:
    parts = filename.replace(".jpg", "").split("_")
    if len(parts) >= 3:
        try:
            lat = float(parts[-2])
            lon = float(parts[-1])
            return (lat, lon)
        except ValueError:
            return None
    return None


def _dms_to_decimal(dms):
    if dms is None or len(dms) != 3:
        return None
    degrees = float(dms[0][0]) / float(dms[0][1])
    minutes = float(dms[1][0]) / float(dms[1][1])
    seconds = float(dms[2][0]) / float(dms[2][1])
    return degrees + minutes / 60.0 + seconds / 3600.0
