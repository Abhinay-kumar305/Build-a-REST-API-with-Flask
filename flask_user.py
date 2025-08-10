from flask import Flask, request, jsonify

app = Flask(__name__)
users = []

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    users.append(data)
    return jsonify({"message": "User added"}), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if 0 <= user_id < len(users):
        data = request.get_json()
        users[user_id] = data
        return jsonify({"message": "User updated"})
    return jsonify({"error": "User not found"}), 404

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if 0 <= user_id < len(users):
        users.pop(user_id)
        return jsonify({"message": "User deleted"})
    return jsonify({"error": "User not found"}), 404

app.run(debug=True)

