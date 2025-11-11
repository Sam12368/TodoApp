from flask import Flask, jsonify, request, send_from_directory
from app.models import TaskManager
import os


app = Flask(__name__)
manager = TaskManager()


@app.route("/")
def index():
    return send_from_directory(
        os.path.join(app.root_path, "..", "static"),
        "index.html")


@app.route("/tasks", methods=["GET"])
def list_tasks():
    return jsonify(manager.get_all())


@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()
    task = manager.add_task(data["title"])
    return jsonify(task), 201


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    deleted = manager.delete_task(task_id)
    if deleted:
        return "", 204
    return jsonify({"error": "Task not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
