from flask import Flask
import json
from datasource.actions import DataSourceAction
from typing import Dict

app = Flask(__name__)


@app.route("/")
def get_courses() -> Dict:
    data = DataSourceAction.get_courses
    return data

@app.route("/courses/<int:course_id>")
def get_course(course_id: int) -> Dict:
    data = DataSourceAction.get_course(__name__, course_id)
    return data





