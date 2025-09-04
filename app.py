from flask import Flask, request, jsonify
import json
import os
from datetime import datetime

app = Flask(__name__)
LOG_FILE = "logs/webhook_log.json"

os.makedirs("logs", exist_ok=True)

@app.route("/webhook", methods=["POST"])
def webhook():
    payload = request.json
    timestamp = datetime.utcnow().isoformat()

    log_entry = {
        "timestamp": timestamp,
        "headers": dict(request.headers),
        "payload": payload
    }

    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(log_entry) + "\n")

    print(f"📩 Webhook received at {timestamp}")
    return jsonify({"status": "received"}), 200

if __name__ == "__main__":
    app.run(port=5000)
