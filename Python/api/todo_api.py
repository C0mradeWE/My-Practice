from flask import Flask, jsonify, request
app = Flask(__name__)
todo_data =[

    {"id":1, "subject":"study lessons", "status":"done"},
    {"id":2, "subject":"learn python", "status":"not done"},
    {"id":3, "subject":"exercise", "status":"in progress"}
]

@app.route('/todos', methods =['POST'] )
def add_todo ():
    user_data =request.get_json()

    if not user_data or "subject" not in user_data:
        return jsonify({"error":"subject is needed"}), 400 # درخواست اشتباه

    new_data ={
        "id":len(todo_data) + 1,
        "subject":user_data["subject"],
        "status":"not done"
    }
    todo_data.append(new_data)
    return jsonify(new_data) ,201 #ساخته شد

@app.route('/todos', methods = ['GET'])
def get_data():
    return jsonify(todo_data)

@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    user_data = request.get_json()
    for t in todo_data:
        if t["id"] == todo_id:
            if "subject" in user_data:
                t["subject"] = user_data["subject"]
            if "status" in user_data:
                t["status"] = user_data["status"]
            return jsonify(t), 200
    return jsonify({"error": "todo not found"}), 404

@app.route('/todos/<int:id>', methods = ['DELETE'])
def todo_delete(id):
    for i in todo_data:
        if i["id"] ==id:
            todo_data.remove(i)
            return jsonify(i), 200
        else:
            return jsonify({"error":"todo not found"})


if __name__=="__main__":
    app.run(debug=True)

        


