# Demo Runbook

See `docs/DEMO_SCRIPT.md` for the full step-by-step.

## Quick Card

| Step | Action | Duration |
|------|--------|----------|
| 1 | Power drone, wait for GPS fix | 30s |
| 2 | Manual flight over grid (or tethered) | 60s |
| 3 | Land drone → auto Wi-Fi offload | 10s |
| 4 | Pipeline processes images | 5s |
| 5 | Dashboard populates with heatmap | 2s |
| 6 | Show Hindi alert | 5s |

**Total: ~2 min**

## Fallback

If drone/camera fails, play `recorded_fallback.mp4` and run:
```bash
python scripts/run_pipeline.py --image ../data/sample_captures/rice_blast.jpg
```
