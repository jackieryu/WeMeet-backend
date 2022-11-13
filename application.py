from flask import Flask, Response, request
import json
from datetime import datetime
import rest_utils
from student_resource import Student

app = Flask(__name__)


##################################################################################################################

# DFF TODO A real service would have more robust health check methods.
# This path simply echoes to check that the app is working.
# The path is /health and the only method is GETs
@app.route("/health", methods=["GET"])
def health_check():
    rsp_data = {"status": "healthy", "time": str(datetime.now())}
    rsp_str = json.dumps(rsp_data)
    rsp = Response(rsp_str, status=200, content_type="application/json")
    return rsp

@app.route("/api/db_book/students/<ID>", methods=["GET"])
def get_student_by_id(ID):
    student = Student()
    rsp_data = student.get_by_id(ID)
    rsp_str = json.dumps(rsp_data, default=str)
    rsp = Response(rsp_str, status=200, content_type="application/json")
    return rsp

##################################################################################################################

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
