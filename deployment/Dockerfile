FROM python:3.14-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1-mesa-glx libglib2.0-0 && \
    rm -rf /var/lib/apt/lists/*

COPY ground_station/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ground_station/ .
COPY models/ models/
COPY data/ data/

EXPOSE 8000 8501

CMD ["sh", "-c", "uvicorn aeris.ingest.wifi_receiver:app --host 0.0.0.0 --port 8000 & streamlit run aeris/dashboard/app.py --server.port 8501 --server.address 0.0.0.0"]
