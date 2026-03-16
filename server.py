from flask import Flask, request, render_template
from EmotionDetection import emotion_detector
import json

app = Flask(__name__)

@app.route("/emotionDetector")
def emotionDetector():
    text = request.args.get("textToAnalyze")
    result = emotion_detector(text)
    dominant_emotion = result["dominant_emotion"]
    
    return f'For the given statement, the system response is. The dominant emotion is {dominant_emotion}.'

@app.route("/")
def render_index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)