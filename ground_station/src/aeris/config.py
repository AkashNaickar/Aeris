from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ingest_port: int = 8000
    ingest_host: str = "0.0.0.0"
    upload_dir: str = "data/ingested"
    sd_watch_dir: str = "data/sd_card"

    ndvi_threshold: float = 0.3
    vari_threshold: float = 0.2

    yolo_model_path: str = "models/yolov8n_aeris.onnx"
    yolo_confidence: float = 0.5
    yolo_iou: float = 0.45

    risk_temp_high: float = 30.0
    risk_humidity_high: float = 80.0

    default_lat: float = 28.6139
    default_lon: float = 77.2090

    alert_language: str = "hindi"

    class Config:
        env_prefix = "AGRISCOUT_"
        env_file = ".env"


settings = Settings()
