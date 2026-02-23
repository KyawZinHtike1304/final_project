from flask import Flask, render_template, request
from emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_route():
    text_to_analyze = request.args.get("textToAnalyze")

    if text_to_analyze is None:
        return "Invalid text! Please try again!", 400

    text_to_analyze = text_to_analyze.strip()
    if not text_to_analyze:
        return "Invalid text! Please try again!", 400

    result = emotion_detector(text_to_analyze)

    # NEW: handle blank input / invalid text from backend
    if result.get("dominant_emotion") is None:
        return "Invalid text! Please try again!", 400

    response_text = (
        "For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response_text


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)