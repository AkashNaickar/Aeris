import json
from pathlib import Path
from aeris.pipeline.orchestrator import run_pipeline
from aeris.geo.heatmap import build_heatmap, results_to_geojson


def seed():
    samples_dir = Path("../data/sample_captures")
    if not samples_dir.exists():
        print("No sample captures directory found")
        return

    results = []
    for img_path in sorted(samples_dir.glob("*.jpg")):
        print(f"Processing {img_path.name}...")
        try:
            result = run_pipeline(img_path)
            results.append(result)
        except Exception as e:
            print(f"  Skipped: {e}")

    geojson = results_to_geojson(results)
    output = Path("demo_output")
    output.mkdir(exist_ok=True)
    (output / "field_health.geojson").write_text(geojson)

    m = build_heatmap(results, output_path=str(output / "field_heatmap.html"))
    print(f"Seeded {len(results)} results → {output.resolve()}")


if __name__ == "__main__":
    seed()
