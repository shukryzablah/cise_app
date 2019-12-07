from cise import app
from flask import jsonify
from cise.models import *

@app.route('/')
def hello_world():
    return 'Hello, World!!'

@app.route('/brandt')
def brandt_route():
    return 'welcome to my route'

@app.route('/get-student-passport')
def get_student_passport():
   join = Student.query.join(Passport).first()
   return jsonify(join.serialize())
