from flask import Flask, request
import json

app = Flask(__name__)

seedNumber: int = 0


@app.route("/", methods=["GET"])
def get_seed():
    global seedNumber
    return str(seedNumber), 200


@app.route("/", methods=["POST"])
def post_seed():
    global seedNumber
    input = json.loads(request.get_data())
    if (
        not isinstance(input, dict)
        or input.get("num") == None
        or not isinstance(input["num"], int)
    ):
        return "", 400
    seedNumber = input["num"]
    return "", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    print("App running on 0.0.0.0:5000")
