# Architecture — 3-Stage Pipeline

```mermaid
flowchart TD
    subgraph Drone["Drone (F450 + ESP32)"]
        NIR[NoIR CAM<br/>Red-filtered NIR] --> CAPTURE
        RGB[RGB CAM] --> CAPTURE
        GPS[NEO-6M] --> CAPTURE
        CAPTURE[Deep-sleep capture<br/>every 5s] --> SD[(SD Card)]
    end

    subgraph Offload["Wi‑Fi Offload (on landing)"]
        SD --> WIFI[FastAPI Receiver<br/>:8000/upload]
        WIFI --> EXIF[EXIF Parser<br/>GPS → lat/lon]
    end

    subgraph Stage1["Stage 1: Macro Anomaly"]
        EXIF --> NDVI[NDVI / VARI Calc]
        NDVI --> THRESH{Stress > τ?}
        THRESH -- No --> HEALTHY[Mark as Healthy]
        THRESH -- Yes --> STRESS[Stressed Zone]
    end

    subgraph Stage2["Stage 2: Micro Disease"]
        STRESS --> CROP[Crop ROI]
        CROP --> YOLO[YOLOv8-nano<br/>Lesion Classification]
        YOLO --> DISEASE[Disease + Confidence]
    end

    subgraph Stage3["Stage 3: Predictive"]
        DISEASE --> FUSION[Microclimate Fusion<br/>Temp / Humidity]
        FUSION --> RISK[Spread Risk Score]
    end

    subgraph Output["Outputs"]
        DISEASE --> MAP[Field Health Heatmap<br/>Folium]
        RISK --> ALERT[Vernacular Alert<br/>Hindi / English]
    end
```

## Key Design Decisions

| Decision | Rationale |
|----------|-----------|
| NDVI as trigger only | Avoids over-reliance on vegetation indices; CNN handles final diagnosis |
| Offline Wi-Fi offload | No cellular dependency — ESP32 creates AP on landing |
| YOLOv8-nano + ONNX | 3 MB model runs at 15 FPS on CPU-only laptop |
| Pydantic Settings | Single source of truth for thresholds, paths, camera params |
| Streamlit + Folium | Rapid dashboard prototyping with free offline tile layers |
