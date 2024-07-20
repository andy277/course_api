from extensions.config_log import config_log
from flask import Flask
import json



filepath = "data/courses.json"

logger = config_log(__name__)

class DataSourceAction():
    @property
    def get_courses(self):
        with open(filepath, "r") as f:
            data = json.load(f)

        if data:
            response = {
                "data": data,
                "status": 200
            }

            logger.info(response)
            return response
        else:
            response = {
                "data": "Not Found",
                "status": 404
            }
            logger.warning(response)
            return response

    def get_course(self, course_id):
        with open(filepath, "r") as f:
            data = json.load(f)

        for course in data:
            if course["id"] == course_id:
                response = {
                    "data": course,
                    "status": 200
                }

                logger.info(response)
                return response
            else:
                response = {
                    "data": "Not Found",
                    "status": 404
                }

                logger.warning(response)
                return response
