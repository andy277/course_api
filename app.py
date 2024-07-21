
from flask import Flask,request
import json
from datasource.actions import DataSourceAction
from typing import Dict

app = Flask(__name__)


@app.route("/api/courses")
def get_courses() -> Dict:
    data = DataSourceAction.get_courses(__name__)
    return data


@app.route("/api/courses/<int:course_id>")
def get_course(course_id: int) -> Dict:
    data = DataSourceAction.get_course(__name__, course_id)
    return data


@app.post("/api/courses/create")
def create_course() -> Dict:
    request_data = request.get_json()
    data = DataSourceAction.create_course(__name__, request_data)
    return data

@app.delete("/api/courses/<int:course_id>")
def delete_course(course_id: int) -> Dict:
    data = DataSourceAction.delete_course(__name__, course_id)
    return data

@app.put("/api/courses/<int:course_id>")
def update_course(course_id: int) -> Dict:
    data = DataSourceAction.update_course(__name__, course_id)
    return data




