'''
Emotion Detection Script

This script calls the Watson NLP API for text analysis.
'''

import json
import requests

def emotion_detector(text_to_analyse):
    '''
    Calls Watson NLP service to detect emotions in the provided text.
    '''
    # pylint: disable=line-too-long
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # pylint: enable=line-too-long
    my_obj = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json=my_obj, headers=headers, timeout=10)

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

    max_score = 0
    dominant_emotion = ""

    for emotion, score in scores.items():
        if score > max_score:
            dominant_emotion = emotion
            max_score = score

    result['dominant_emotion'] = dominant_emotion
    return result
