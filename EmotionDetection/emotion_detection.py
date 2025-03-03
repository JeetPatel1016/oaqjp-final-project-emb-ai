import requests
import json
def emotion_detector(text_to_analyse):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myObj = { "raw_document": { "text": text_to_analyse } }
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(URL, json=myObj, headers=headers)
    if response.status_code == 400:
        return {
            'anger': None,
            'sadness': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'dominant_emotion': None
        }
    
    formatted_response = json.loads(response.text)
    scores = formatted_response['emotionPredictions'][0]['emotion']
    result = scores.copy()
    maxScore = 0
    dominantEmotion = ""
    for emotion in scores:
        if(scores[emotion] > maxScore):
            dominantEmotion = emotion
            maxScore = scores[emotion]
    result['dominant_emotion'] = dominantEmotion

    return result