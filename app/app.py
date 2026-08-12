from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify(
        {
            "application": "AI Cloud Labs CI/CD Platform",
            "status": "running",
            "version": os.getenv("APP_VERSION", "development"),
            "hostname": socket.gethostname(),
        }
    )


@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200


@app.route("/ready")
def ready():
    return jsonify({"status": "ready"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
