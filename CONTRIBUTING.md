# Contributing to Aeris

## Workflow

1. **Branch-per-module**: `feat/ndvi`, `feat/yolo`, `feat/dashboard`, `feat/firmware`
2. **PRs require**: one peer review + passing lint (`ruff check .`)
3. **Commit style**: `[module] verb — e.g. [ingest] add Wi-Fi receiver endpoint`

## Code Review Checklist

- [ ] No hardcoded paths — use `config.py`
- [ ] GPS EXIF parsing handles missing tags gracefully
- [ ] NDVI division by zero guarded
- [ ] YOLO inference uses `.onnx` for edge CPU perf
- [ ] Dashboard loads without internet (offline tiles)
