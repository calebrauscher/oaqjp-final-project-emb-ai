from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET"])
def emotion_detection_api():
    text_to_analyze = request.args.get("textToAnalyze", "")
    if not text_to_analyze.strip():
        return "Please provide valid text for emotion detection."
    
    try:
        emotion_scores = emotion_detector(text_to_analyze)

        # Format the emotion results as in the required output
        formatted_scores = ", ".join(
            [f"'{emotion}': {score}" for emotion, score in emotion_scores.items() if emotion != "dominant_emotion"]
        )

        # Final response string
        response_text = (
            f"For the given statement, the system response is {formatted_scores}. "
            f"The dominant emotion is {emotion_scores.get('dominant_emotion')}."
        )

        return response_text

    except Exception as e:
        return f"Error processing request: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
