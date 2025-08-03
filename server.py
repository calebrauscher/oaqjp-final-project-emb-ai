"""Emotion Detection Flask Application.
"""
from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    """Index html handler."""
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET"])
def emotion_detection_api():
    """Emotion Detetction"""
    text_to_analyze = request.args.get("textToAnalyze", "")

    try:
        emotion_scores = emotion_detector(text_to_analyze)
        if emotion_scores.get("dominant_emotion") is None:
            return "Invalid text! Please try again!"

        # Format the emotion results as in the required output
        formatted_scores = ", ".join(
            [f"'{emotion}': {score}"
            for emotion, score in emotion_scores.items()
            if emotion != "dominant_emotion"]
        )

        # Final response string
        response_text = (
            f"For the given statement, the system response is {formatted_scores}. "
            f"The dominant emotion is {emotion_scores.get('dominant_emotion')}."
        )

        return response_text

    except (KeyError, TypeError):
        return "Error processing the emotion data. Please ensure the text is valid.", 500

    except ValueError as ve:
        return f"Value error: {str(ve)}", 400

if __name__ == "__main__":
    app.run(debug=True)
