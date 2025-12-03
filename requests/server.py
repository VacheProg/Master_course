from flask import Flask, request, jsonify

app = Flask(__name__)

# Fake database
users = {
    1: {"name": "Anna", "age": 25},
    2: {"name": "Vache", "age": 30}
}

@app.get("/users")
def get_users():
    return jsonify(users)

@app.get("/users/<int:user_id>")
def get_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)

@app.post("/users")
def create_user():
    data = request.json
    new_id = max(users.keys()) + 1
    users[new_id] = data
    return jsonify({"id": new_id, "created": data}), 201

@app.put("/users/<int:user_id>")
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    users[user_id] = request.json
    return jsonify({"updated": users[user_id]})

@app.delete("/users/<int:user_id>")
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    deleted = users.pop(user_id)
    return jsonify({"deleted": deleted})

if __name__ == "__main__":
    app.run(debug=True)
