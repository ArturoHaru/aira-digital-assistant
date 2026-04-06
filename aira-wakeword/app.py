# app.py

from flask import Flask, jsonify, request

from wakeword_service import process_audio

app = Flask(__name__)


@app.route("/")
def hello():
    return "<p>Hello</p>"


@app.route("/check-wakeword", methods=["POST"])
def check_wakeword():
    if "audio" not in request.files:
        return jsonify({"error": "File mancante"}), 400

    file = request.files["audio"]

    try:
        # Passiamo direttamente l'oggetto file (stream in memoria)
        found = process_audio(file)
        return jsonify({"wakeword_detected": found})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
