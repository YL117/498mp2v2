import subprocess
from flask import Flask, request
import json
import socket

app = Flask(__name__)


@app.route("/", methods=["GET"])
def get_seed():
    return socket.gethostname(), 200


@app.route("/", methods=["POST"])
def post_seed():
    subprocess.Popen(["python3", "stress_cpu.py"])
    return "", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    print("App running on 0.0.0.0:5000")
