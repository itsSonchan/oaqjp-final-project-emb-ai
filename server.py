from flask import Flask, request, render_template
from EmotionDetection import emotion_detector
import json

app = Flask(__name__)

@app.route("/emotionDetector")
def emotionDetector():
    text = request.args.get("textToAnalyze")
    result = emotion_detector(text)
    dominant_emotion = result["dominant_emotion"]

    return f"For the given statement, the system response is 'anger': {result['anger']}, 'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} and 'sadness': {result['sadness']}. The dominant emotion is <strong>{dominant_emotion}</strong>."

@app.route("/")
def render_index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)