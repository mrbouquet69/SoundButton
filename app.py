from flask import Flask, request, jsonify

app = Flask(__name__)

WEBHOOK_SECRET = "yoursecret"
latest_event = {}

@app.route("/trigger", methods=["POST"])
def trigger():
    global latest_event
    data = request.json
    if not data or data.get("secret") != WEBHOOK_SECRET:
        return jsonify({"error": "Unauthorized or invalid data"}), 403

    latest_event = data
    print("Received event:", data)
    return jsonify({"status": "ok"})

@app.route("/get-latest", methods=["GET"])
def get_latest():
    return jsonify(latest_event)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
