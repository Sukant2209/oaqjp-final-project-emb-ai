'''This module is for making and deploying a flask application'''

from flask import Flask , request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods = ["GET"])
def emotion_detect():

    '''Runs emotion_detector function and provide formatted user friendly reponse'''

    text_to_analyze = request.args.get("textToAnalyze")

    resp = emotion_detector(text_to_analyze)

    return f'''For the given statement, the system response is 'anger': {resp.get('anger')},
    'disgust': {resp.get('disgust')}, 'fear': {resp.get('fear')}, 'joy': {resp.get('joy')}
    and 'sadness': {resp.get('sadness')}. 
    The dominant emotion is <b>{resp.get('dominant_emotion')}</b>'''

@app.route("/")
def get_index():
    '''This will render the index html page'''
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
