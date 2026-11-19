
import os
import joblib

from flask import Flask, request, jsonify , render_template

from preprocessing import preprocess_complaint


# Initialize Flask
app = Flask(__name__)


# Model artifact paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "model_artifacts",
    "final_svc_model.pkl"
)

VECTORIZER_PATH = os.path.join(
    BASE_DIR,
    "model_artifacts",
    "tfidf_unigram.pkl"
)


# Check artifact availability
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(
        f"Model file not found: {MODEL_PATH}"
    )

if not os.path.exists(VECTORIZER_PATH):
    raise FileNotFoundError(
        f"Vectorizer file not found: {VECTORIZER_PATH}"
    )


# Load trained model and vectorizer
model = joblib.load(MODEL_PATH)
tfidf_vectorizer = joblib.load(VECTORIZER_PATH)


# Validate feature compatibility
expected_features = model.n_features_in_
available_features = len(tfidf_vectorizer.vocabulary_)

if expected_features != available_features:
    raise ValueError(
        f"Feature mismatch! Model expects {expected_features}, "
        f"but vectorizer has {available_features} features."
    )


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "model": "Balanced Linear SVC",
        "vectorizer": "TF-IDF Unigram",
        "features": int(expected_features)
    })


@app.route("/predict", methods=["POST"])
def predict():

    try:

        data = request.get_json(silent=True)

        if not data:
            return jsonify({
                "error": "Please provide complaint text."
            }), 400

        complaint = data.get("complaint", "")

        if not isinstance(complaint, str) or not complaint.strip():
            return jsonify({
                "error": "Complaint text cannot be empty."
            }), 400

        # Step 1: Preprocess complaint
        processed_text = preprocess_complaint(complaint)

        if not processed_text:
            return jsonify({
                "error": "No meaningful text remains after preprocessing."
            }), 400

        # Step 2: TF-IDF transformation
        complaint_vector = tfidf_vectorizer.transform(
            [processed_text]
        )

        # Step 3: Model prediction
        prediction = model.predict(complaint_vector)[0]

        return jsonify({
            "success": True,
            "original_complaint": complaint,
            "predicted_category": str(prediction),
            "processed_text": processed_text
        })

    except Exception as e:

        app.logger.exception("Prediction failed")

        return jsonify({
            "success": False,
            "error": "Prediction failed. Please check the server logs."
        }), 500


@app.route("/classify")
def classify_page():
    return render_template("classify.html")


@app.route("/performance")
def performance_page():
    return render_template("performance.html")


@app.route("/about")
def about_page():
    return render_template("about.html")

if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )
