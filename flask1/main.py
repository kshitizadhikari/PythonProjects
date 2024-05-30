from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Home"


@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "John Doe",
    }

    extra_data = request.args.get("role")

    if extra_data:
        user_data["role"] = extra_data
    return jsonify(user_data), 200


@app.route("/create-user", methods=["POST"])
def create_user():
    if request.method == "POST":
        data = request.get_json()
        return jsonify(data), 201


if __name__ == "__main__":
    app.run(debug=True)

