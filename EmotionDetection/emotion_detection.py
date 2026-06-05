import requests

#URL: 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
#Headers: {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
#Input json: { "raw_document": { "text": text_to_analyze } }

EMOTION_API_URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

def emotion_detector(text):
    """Detects the emotion of the given text using the Watson Emotion API."""
    payload = {"raw_document": {"text": text}}
    response = requests.post(EMOTION_API_URL, headers=HEADERS, json=payload)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.status_code, "message": response.text}