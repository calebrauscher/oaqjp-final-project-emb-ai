"""The function to run emotion detection using the appropriate Emotion Detection function
"""
import requests
import json

def emotion_detector(text_to_analyze):
    """
    Sends a POST request to the Watson NLP EmotionPredict endpoint
    and returns the response's 'text' attribute.

    Args:
        text_to_analyze (str): The input text for emotion analysis.

    Returns:
        dict: The 'text' field from the response containing emotion prediction.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "Content-Type": "application/json",
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(url, headers=headers, json=input_json)
    
    # Handle bad request (400) from server
    
    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
    
    # Ensure the request was successful
    if response.status_code == 200:
        result = response.json()
        emotions = result.get("emotionPredictions", [])
        if emotions:
            results = emotions[0]['emotion'] | {'dominant_emotion': dominant_emotion(emotions[0]['emotion'])}
            return results
        else:
            return {"error": "No emotion predictions returned."}
    else:
        raise Exception(f"Request failed with status code {response.status_code}: {response.text}")

def dominant_emotion(emotions):
    return sorted(emotions.items(), key=lambda item: item[1], reverse=True)[0][0]