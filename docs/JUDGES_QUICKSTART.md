# Judges' Quickstart — 60 Seconds

```bash
# 1. Install
cd aeris/ground_station
pip install -r requirements.txt

# 2. Run pipeline on sample image
python scripts/run_pipeline.py --image ../data/sample_captures/rice_blast.jpg

# 3. Launch dashboard
streamlit run src/aeris/dashboard/app.py

# Expected output:
# - Terminal: NDVI=0.32, Disease=Rice Blast (91%), Risk=HIGH
# - Browser: Folium map with red/green markers + alert in Hindi/English
```

## Key files for judges

| File | Why |
|------|-----|
| `src/aeris/pipeline/orchestrator.py` | The 3-stage pipeline composition |
| `src/aeris/pipeline/stage1_macro.py` | NDVI/VARI calculation |
| `src/aeris/pipeline/stage2_micro.py` | YOLOv8 inference |
| `src/aeris/dashboard/app.py` | Streamlit + Folium heatmap |
| `firmware/esp32_nir_cam/src/main.cpp` | Deep-sleep capture + GPS |
