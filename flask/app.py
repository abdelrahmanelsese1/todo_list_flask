from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

tasks = []

@app.route('/', methods=['GET'])
def list_home():
    return jsonify({
        "taskslist": tasks
    })


@app.route('/add_task', methods=['POST'])
def add_task():
    task_id = request.json.get('task_id')
    title = request.json.get('title')
    status = request.json.get('status')
    tasks.append({
        'task_id':task_id,
        'title':title,
        'status':status
    })
    return jsonify({
        "taskslist": tasks
    })

@app.route('/update_task/<int:id>', methods=['PUT'])
def update_task(id):
    for task in tasks:
        if task['task_id'] == id:
            updated_list = task
            updated_list['task_id'] = request.json.get('task_id')
            updated_list['title'] = request.json.get('title')
            updated_list['status'] = request.json.get('status')

            return jsonify({
                        "taskslist": updated_list
                })

    return jsonify({
        "error": "the task with this id not found"
    })

@app.route('/delete_task/<int:id>', methods=['DELETE'])
def delete_task(id):
    for task in tasks:
        if task['task_id'] == id:
            deleted_list = task
            tasks.remove(deleted_list)
            return jsonify({
                "msg": "task deleted successfully"
        })
    return jsonify({
                "error": "the task with this id not found"
        })


app.run(host='127.0.0.1', port=5000, debug=True)


