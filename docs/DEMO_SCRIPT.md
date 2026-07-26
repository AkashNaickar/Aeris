# Demo Runbook

## Setup (5 min)

1. Place fake-disease potted plant on marked grid square
2. Start ground station: `streamlit run src/aeris/dashboard/app.py`
3. Power drone — wait for ESP32 AP to appear
4. Connect laptop to `Aeris-AP` Wi-Fi

## Live Demo Flow (3 min)

| # | Action | Screens Says |
|---|--------|-------------|
| 1 | Launch drone manually over grid | _Dashboard: "Waiting for capture..."_ |
| 2 | Drone captures NoIR + RGB image | _Console logs GPS coords_ |
| 3 | Drone lands — auto-connects to GS | _Dashboard: "Processing..."_ |
| 4 | Stage 1 runs — NDVI stress map | _Red overlay on diseased leaf_ |
| 5 | Stage 2 runs — YOLO boxes disease | _"Late Blight — 94% confidence"_ |
| 6 | Stage 3 fuses temp/humidity | _"Spread Risk: HIGH"_ |
| 7 | Map populates with marker | _Red pin with disease name_ |
| 8 | Alert generated | Hindi SMS appears on screen |

## Backup (if drone fails)

Play `demo/recorded_fallback.mp4` showing the full pipeline with pre-captured images.
