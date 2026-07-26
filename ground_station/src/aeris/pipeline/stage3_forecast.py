from aeris.config import settings


def compute_risk_score(
    disease: str,
    confidence: float,
    temperature: float | None = None,
    humidity: float | None = None,
) -> dict:
    base_score = confidence
    if temperature is None:
        temperature = 28.0
    if humidity is None:
        humidity = 65.0

    env_factor = 0.0
    if temperature > settings.risk_temp_high:
        env_factor += 0.3
    if humidity > settings.risk_humidity_high:
        env_factor += 0.3

    if disease == "Healthy":
        risk = 0.0
        level = "NONE"
    else:
        raw = base_score * 0.7 + env_factor * 0.3
        risk = round(min(raw, 1.0), 2)
        if risk < 0.3:
            level = "LOW"
        elif risk < 0.6:
            level = "MEDIUM"
        else:
            level = "HIGH"

    return {
        "risk_score": risk,
        "risk_level": level,
        "temperature": temperature,
        "humidity": humidity,
    }
