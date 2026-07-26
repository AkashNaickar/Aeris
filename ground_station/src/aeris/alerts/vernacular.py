ALERTS_HINDI = {
    "LOW": "आपके खेत में रोग का हल्का खतरा है। निगरानी जारी रखें।",
    "MEDIUM": "सावधान! फसल में रोग फैलने की संभावना है। तुरंत निरीक्षण करें।",
    "HIGH": "चेतावनी! रोग तेजी से फैल सकता है। तत्काल उपाय करें।",
    "NONE": "आपकी फसल स्वस्थ है। कोई कार्रवाई आवश्यक नहीं है।",
}

ALERTS_ENGLISH = {
    "LOW": "Low disease risk detected in your field. Continue monitoring.",
    "MEDIUM": "Caution! Disease may be spreading. Inspect immediately.",
    "HIGH": "Warning! Disease spread risk is high. Take action now.",
    "NONE": "Your crop is healthy. No action needed.",
}


def generate_alert(risk_level: str, disease: str, language: str = "hindi") -> str:
    alerts = ALERTS_HINDI if language == "hindi" else ALERTS_ENGLISH
    base = alerts.get(risk_level, ALERTS_ENGLISH[risk_level])
    if disease != "Healthy" and disease != "Unknown":
        disease_msg = (
            f"रोग: {disease}. "
            if language == "hindi"
            else f"Disease: {disease}. "
        )
        return disease_msg + base
    return base
