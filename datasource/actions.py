from extensions.config_log import config_log
from flask import request
import json
from typing import Dict


filepath = "data/courses.json"

logger = config_log(__name__)

class DataSourceAction():
    def get_courses(self) -> Dict:
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

    def get_course(self, course_id) -> Dict:
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

        return {"data": "Not Found", "status": 404}

    def create_course(self, new_course) -> Dict:
        with open(filepath, "r") as f:
            data = json.load(f)

        id_list = [course["id"] for course in data]

        id = max(id_list) + 1

        created_course = {"course": new_course, "id": id }
        data.append(created_course)

        data = json.dumps(data)

        with open(filepath, "w") as f:
            f.write(data)

        if data:
            response = {
                "message": "New Course Created",
                "status": 200
            }
            logger.info(response)
        else:
            response = {
                "message": "Failed to create new course",
                "status": 404
            }
            logger.warning(response)

        return response

    def delete_course(self, course_id) -> Dict:
        with open(filepath, "r") as f:
            data = json.load(f)

            filtered_tasks = [course for course in data if course["id"] != course_id]

        data = json.dumps(filtered_tasks)

        with open(filepath, "w") as f:
            f.write(data)

        if data:
            response = {
                "message": "Course Deleted",
                "status": 200
            }
            logger.info(response)
        else:
            response = {
                "message": "Failed to delete course",
                "status": 404
            }
            logger.warning(response)

        return response

    def update_course(self, course_id) -> Dict:
        new_course = request.get_json()

        with open(filepath, "r") as f:
            data = json.load(f)

            for course in data:
                if course["id"] == course_id:
                    course["course"] = new_course

            data = json.dumps(data)

        with open(filepath, "w") as f:
            f.write(data)

        if data:
            response = {
                "message": "Course Updated",
                "status": 200
            }
            logger.info(response)
        else:
            response = {
                "message": "Update failed",
                "status": 404
            }
            logger.warning(response)

        return response
