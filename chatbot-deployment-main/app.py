from flask import Flask, render_template, request, jsonify, Response

from chat import get_response

app = Flask(__name__)

@app.get("/")
def index_get():
    response = Response(render_template("base.html"))
    response.headers["X-Frame-Options"] = "ALLOWALL"  # Allows embedding in iframe
    return response

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True)
