import folium
from folium.plugins import HeatMap
from pathlib import Path
import json

from aeris.config import settings


def build_heatmap(results: list[dict], output_path: str | Path | None = None) -> folium.Map:
    center_lat = settings.default_lat
    center_lon = settings.default_lon
    heat_data = []
    markers = []

    for r in results:
        if r.get("gps"):
            lat, lon = r["gps"]
            risk = r.get("stage3", {}).get("risk_score", 0)
            disease = r.get("stage2", {}).get("disease", "Unknown")
            heat_data.append([lat, lon, risk])
            color = "red" if risk > 0.6 else "orange" if risk > 0.3 else "green"
            markers.append((lat, lon, disease, color))

    m = folium.Map(location=[center_lat, center_lon], zoom_start=16,
                   tiles="OpenStreetMap")

    if heat_data:
        HeatMap(heat_data, radius=15, blur=10, max_zoom=1).add_to(m)

    for lat, lon, disease, color in markers:
        folium.Marker(
            [lat, lon],
            popup=disease,
            icon=folium.Icon(color=color, icon="leaf", prefix="fa"),
        ).add_to(m)

    if output_path:
        m.save(str(output_path))

    return m


def results_to_geojson(results: list[dict]) -> str:
    features = []
    for r in results:
        if not r.get("gps"):
            continue
        lat, lon = r["gps"]
        features.append({
            "type": "Feature",
            "geometry": {"type": "Point", "coordinates": [lon, lat]},
            "properties": {
                "disease": r.get("stage2", {}).get("disease"),
                "risk": r.get("stage3", {}).get("risk_level"),
                "image": r.get("image"),
            },
        })
    return json.dumps({"type": "FeatureCollection", "features": features}, indent=2)
