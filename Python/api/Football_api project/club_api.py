from flask import Flask, jsonify, request
from api_data import players

app = Flask(__name__)

@app.route('/icons', methods=['GET'])
def get_data():
    return jsonify(players)

@app.route('/icons', methods=['POST'])
def post_data():
    user_data = request.get_json()
    if not user_data or "name" not in user_data:
        return jsonify({"error": "name is required"}), 400
    new_player = {
        "id": len(players) + 1,
        "name": user_data["name"],
        "position": user_data.get("position", ""),
        "nationality": user_data.get("nationality", "")
    }
    players.append(new_player)
    return jsonify(new_player), 201

@app.route('/icons/<int:player_id>', methods=['PUT'])
def put_data(player_id):
    user_data = request.get_json()
    if not user_data:
        return jsonify({"error": "player data is required"}), 400
    for i in players:
        if i["id"] == player_id:
            if "name" in user_data:
                i["name"] = user_data["name"]
            if "position" in user_data:
                i["position"] = user_data["position"]
            if "nationality" in user_data:
                i["nationality"] = user_data["nationality"]
            return jsonify(i), 200
    return jsonify({"error": "player not found"}), 404

@app.route('/icons/<int:player_id>', methods=['DELETE'])
def remove(player_id):
    for i in players:
        if i["id"] == player_id:
            players.remove(i)
            return jsonify(i), 200
    return jsonify({"error": "id not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)

"""


http://127.0.0.1:5000/icons


"""