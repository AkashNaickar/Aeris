import math


def latlon_to_utm(lat: float, lon: float) -> tuple[float, float, str]:
    zone = int((lon + 180) / 6) + 1
    hemisphere = "N" if lat >= 0 else "S"
    lat_rad = math.radians(lat)
    lon_rad = math.radians(lon)

    a = 6378137.0
    f = 1 / 298.257223563
    k0 = 0.9996

    e = math.sqrt(2 * f - f ** 2)
    e2 = e * e
    e4 = e2 * e2
    e6 = e4 * e2

    N = a / math.sqrt(1 - e2 * math.sin(lat_rad) ** 2)
    T = math.tan(lat_rad) ** 2
    C = e2 * math.cos(lat_rad) ** 2 / (1 - e2)
    A = math.cos(lat_rad) * (lon_rad - math.radians((zone - 1) * 6 - 180 + 3))

    M = a * (
        (1 - e2 / 4 - 3 * e4 / 64 - 5 * e6 / 256) * lat_rad
        - (3 * e2 / 8 + 3 * e4 / 32 + 45 * e6 / 1024) * math.sin(2 * lat_rad)
        + (15 * e4 / 256 + 45 * e6 / 1024) * math.sin(4 * lat_rad)
        - (35 * e6 / 3072) * math.sin(6 * lat_rad)
    )

    easting = k0 * N * (A + (1 - T + C) * A ** 3 / 6
                        + (5 - 18 * T + T ** 2 + 72 * C - 58 * e2) * A ** 5 / 120) + 500000.0
    northing = k0 * (M + N * math.tan(lat_rad) * (
        A ** 2 / 2 + (5 - T + 9 * C + 4 * C ** 2) * A ** 4 / 24
        + (61 - 58 * T + T ** 2 + 600 * C - 330 * e2) * A ** 6 / 720
    ))
    if hemisphere == "S":
        northing += 10000000.0

    return round(easting, 2), round(northing, 2), f"{zone}{hemisphere}"


def haversine_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    R = 6371000
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat / 2) ** 2
         + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2))
         * math.sin(dlon / 2) ** 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c
