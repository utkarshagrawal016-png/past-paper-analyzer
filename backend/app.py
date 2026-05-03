from flask import Flask, request, jsonify
from utils import analyze_text, generate_plan
import pdfplumber
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
def extract_text(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

@app.route("/analyze", methods=["POST"])
def analyze():
    files = request.files.getlist("files")
    
    all_text = ""
    for file in files:
        all_text += extract_text(file)

    topic_counts = analyze_text(all_text)
    plan = generate_plan(topic_counts)

    return jsonify({
        "topics": topic_counts,
        "plan": plan
    })

if __name__ == "__main__":
    app.run(debug=True)