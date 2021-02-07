import json
import jwt

from flask_socketio import emit
from passlib.hash import sha256_crypt
from flask import jsonify, request
from flask_cors import cross_origin

from app import app, socketio
from app.models import User, Table
from app.config import Config


def token_required(func):
    def wrapper(*args, **kwargs):
        username = jwt.decode(request.headers["Authorization"], Config.SECRET_KEY, algorithms=["HS256"])["username"]
        if username == request.headers["Username"]:
            value = func(*args, **kwargs)
            return value
    return wrapper


@app.route('api/get-token', methods=["POST"])
@cross_origin()
def auth():
    data = json.loads(request.data.decode("utf-8"))
    for user in User.objects:
        if data["username"] == user.username and sha256_crypt.verify(data["password"], user.password):
            token = jwt.encode({"username": user.username}, Config.SECRET_KEY, algorithm="HS256")
            return jsonify(token=token)


@app.route('api/get-table')
@cross_origin()
@token_required
def get_table():
    table = []
    for row in Table.objects:
        table.append(row)
    return jsonify(table=table)


@socketio.on("CHANGE_CELL")
def save_cell(data):
    value = data["value"]
    if "title" in value.keys():
        Table.objects(id=data["id"]).update(set__title=value["title"])
        emit("CHANGE_TITLE", {"id": data["id"], "value": value["title"]}, broadcast=True)
    elif "date" in value.keys():
        Table.objects(id=data["id"]).update(set__date=value["date"])
        emit("CHANGE_DATE", {"id": data["id"], "value": value["date"]}, broadcast=True)
    elif "number" in value.keys():
        if value["number"] == "":
            value["number"] = 0
        Table.objects(id=data["id"]).update(set__number=value["number"])
        emit("CHANGE_NUMBER", {"id": data["id"], "value": value["number"]}, broadcast=True)


@socketio.on("CHANGE_CELLS")
def save_cells(data):
    for id_ in data["ids"]:
        Table.objects(id=id_).update(set__status=data["value"])
    emit("CHANGE_STATUS", {"ids":  data["ids"], "value": data["value"]}, broadcast=True)


@socketio.on('ADD_ROW')
def add_row(data):
    newRow = Table(number=0, title='Default title', date=data, status="New").save()
    json_row = newRow.to_json()
    emit("ADD_ROW", json_row, broadcast=True)


@socketio.on("DELETE_ROWS")
def delete_rows(ids):
    for id_ in ids:
        Table.objects(id=id_).delete()
    emit("DELETE_ROWS", ids, broadcast=True)
