'''
This module returns Emotion Detetction response using the standard
Watson NLP library
'''

import json
import requests

def emotion_detector(text_to_analyse):

    '''
    This method calles Emotion Predict function in Watson NLP library
    and return a text reponse
    '''

    url = ('https://sn-watson-emotion.labs.skills.network/'
    'v1/watson.runtime.nlp.v1/NlpService/EmotionPredict')

    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    json_obj = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, headers= headers, json = json_obj, timeout = 5)

    if response.status_code == 400:
        return {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}
    
    json_resp = json.loads(response.text)
    
    emotion_resp = json_resp["emotionPredictions"][0]["emotion"]

    emotion_resp['dominant_emotion'] = max(emotion_resp, key = emotion_resp.get)

    return emotion_resp