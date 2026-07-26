import argparse
from pathlib import Path
from aeris.pipeline.orchestrator import run_pipeline, format_result


def main():
    parser = argparse.ArgumentParser(description="Aeris Pipeline CLI")
    parser.add_argument("--image", type=str, required=True, help="Path to input image")
    args = parser.parse_args()

    image_path = Path(args.image)
    if not image_path.exists():
        print(f"Error: {image_path} not found")
        return 1

    result = run_pipeline(image_path)
    print(format_result(result))
    return 0


if __name__ == "__main__":
    exit(main())
