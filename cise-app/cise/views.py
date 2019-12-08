from cise import app
from cise.models import Student, Passport

from flask import jsonify, request, redirect, url_for


@app.route('/')
def hello_world():
    return Passport.query.with_entities(Passport.country).distinct()


@app.route('/brandt')
def brandt_route():
    return 'welcome to my route'


@app.route('/get-student-passport')
def get_student_passport():
    join = Student.query.join(Passport).first()
    return jsonify(join.serialize())


@app.route('/search', methods=['POST'])
def handle_search_request():
    return redirect(
        url_for("get_search_results", **request.json, _method="GET")
    )


@app.route('/search-results', methods=["GET", "POST"])
def get_search_results():
    # First get possible values to filter by.
    first_name = request.args.get("first_name", None)
    country = request.args.get("country", None)
    # Then construct the appropriate query.
    query = Student.query.join(Student.passport_id)
    if(country is not None):
        query = query.filter(Passport.country == country)
    if(first_name is not None):
        query = query.filter(Student.legal_first == first_name)
    # Execute the query and return response
    results = query.all()
    return jsonify([result.serialize() for result in results])
