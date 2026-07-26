# Aeris – Offline Multimodal Drone for Predictive Crop Disease Mapping

Aeris is an autonomous, offline drone-based system that acts as a "Data Mule" over agricultural fields. It captures GPS-tagged NoIR + RGB imagery and runs a **3-stage multimodal AI pipeline** on a local ground station to detect early plant stress, classify diseases, and generate actionable field health heatmaps — all without internet connectivity.

## Architecture Overview

```
┌─────────────────┐     ┌──────────────────────┐     ┌─────────────────┐
│   Drone (F450)  │────▶│  Ground Station       │────▶│  Farmer Alert   │
│  ┌───────────┐  │ Wi-Fi│  ┌────────────────┐  │     │  (SMS/App)      │
│  │NoIR ESP32 │  │offload│  │ Stage 1: NDVI  │  │     └─────────────────┘
│  │ + RGB ESP32│  │      │  │ (Macro Stress) │  │
│  │ + NEO-6M  │  │      │  ├────────────────┤  │
│  │ + SD Card │  │      │  │ Stage 2: YOLOv8│  │
│  └───────────┘  │      │  │ (Micro Disease)│  │
│  100% Offline   │      │  ├────────────────┤  │
└─────────────────┘      │  │ Stage 3: Risk  │  │
                          │  │ (Forecast)     │  │
                          │  ├────────────────┤  │
                          │  │ Dashboard      │  │
                          │  │ (Folium +      │  │
                          │  │  Streamlit)    │  │
                          │  └────────────────┘  │
                          └──────────────────────┘
```

## Quick Start

```bash
cd ground_station
pip install -r requirements.txt
python scripts/run_pipeline.py --image data/sample_captures/test_ndvi.jpg
streamlit run src/aeris/dashboard/app.py
```

## Repository Structure

```
aeris/
├── firmware/          # ESP32-CAM Arduino code (NoIR + RGB + GPS)
├── ground_station/    # Python AI pipeline + dashboard
├── models/            # Trained YOLOv8 weights + ONNX exports
├── notebooks/         # Jupyter exploration & training logs
├── data/              # Sample captures & PlantVillage subset
├── demo/              # Demo assets & runbook
├── docs/              # Architecture, wiring, judging guides
└── deployment/        # Docker + systemd for edge deployment
```

## Key Technologies

- **Hardware:** ESP32-CAM (OV2640), ESP32-NoIR-CAM, NEO-6M GPS, F450 frame
- **Vision:** OpenCV, NDVI/VARI, YOLOv8-nano (Ultralytics)
- **Pipeline:** FastAPI ingestion, Pydantic config, asyncio orchestration
- **Mapping:** Folium + Streamlit for interactive heatmaps
- **Deployment:** Docker, systemd, offline-first design

## License

MIT
