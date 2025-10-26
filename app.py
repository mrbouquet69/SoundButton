from flask import Flask, request, jsonify

app = Flask(__name__)

# Optional secret key to secure requests
WEBHOOK_SECRET = "yoursecret"

@app.route("/trigger", methods=["POST"])
def trigger():
    data = request.json
    if not data:
        return jsonify({"error": "No data"}), 400

    # Optional security check
    if data.get("secret") != WEBHOOK_SECRET:
        return jsonify({"error": "Unauthorized"}), 403

    # Example: store latest event in memory (or database)
    global latest_event
    latest_event = data
    print("Received event:", data)
    return jsonify({"status": "ok"})

@app.route("/get-latest", methods=["GET"])
def get_latest():
    return jsonify(latest_event if 'latest_event' in globals() else {})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
