#!/usr/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Flask API!"


@app.route("/data", methods=["GET"])
def data():
    # Return a list of all usernames (keys of users dict), empty list if none
    return jsonify(list(users.keys()))


@app.route("/status", methods=["GET"])
def status():
    return "OK"


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()
    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]

    # If user exists, overwrite (or you can choose to reject duplicates)
    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    return jsonify({"message": "User added", "user": users[username]}), 201


if __name__ == "__main__":
    app.run()
