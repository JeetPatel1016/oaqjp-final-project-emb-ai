from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route('/')
def render_homepage():
    return render_template('index.html')

@app.route('/emotionDetector')
def get_emotion_results():
    text_to_analyze = request.args.get('textToAnalyze')
    data = emotion_detector(text_to_analyze)
    if data['dominant_emotion'] is None:
        return "Invalid text! Please try again!."
    
    return (
        f"Based on the analysis, the detected emotion is {data['dominant_emotion']}. "
        f"Here are the probability scores: "
        f"Anger: {data['anger']:.2f}, "
        f"Sadness: {data['sadness']:.2f}, "
        f"Disgust: {data['disgust']:.2f}, "
        f"Fear: {data['fear']:.2f}, "
        f"Joy: {data['joy']:.2f}."
    )
if __name__ == "__main__":
    app.run()