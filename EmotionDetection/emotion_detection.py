'''Make API call for emotion detection and return result'''

import requests, json

def emotion_detector(text_to_analyze):
    '''function that makes the API call'''
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    
    response = requests.post(url, headers=header, json=input_json)
    json_result = response.json()
    emotions = json_result["emotionPredictions"][0]["emotion"]
    dominant_emotion = max(emotions, key=emotions.get)
    emotions["dominant_emotion"] = dominant_emotion

    return emotions