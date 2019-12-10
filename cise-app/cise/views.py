from cise import app
from cise.models import Student, Passport
#from cise.models import Example

from flask import jsonify, request, redirect, url_for, render_template, json


@app.route('/')
def render_home():
    return render_template("home.html")


@app.route('/hello')
def hello_world():
    return Passport.query.with_entities(Passport.country).distinct()


@app.route('/brandt')
def brandt_route():
    return 'welcome to my route'


@app.route('/test')
def test_route():
    return render_template("layout.html")


@app.route('/get-student-passport')
def get_student_passport():
    join = Student.query.join(Passport).first()
    return jsonify(join.serialize())


#####################################################
# Handle the search from homepage and the response. #
#####################################################

@app.route('/search', methods=['POST'])
def handle_search_request():
    return redirect(
        url_for("render_results", **request.form, _method="GET")
    )


def get_search_results(**kwargs):
    # First get possible values to filter by.
    first_name = kwargs.pop("first_name", None)
    country = kwargs.pop("country", None)
    # Then construct the appropriate query by filtering.
    query = Student.query.join(Student.passport_id)
    if(first_name is not None and first_name != ""):
        query = query.filter(Student.legal_first == first_name)
    if(country is not None and country != ""):
        query = query.filter(Passport.country == country)
    # Execute the query and return response.
    results = query.all()
    return json.dumps([result.serialize() for result in results])


@app.route('/search-results')
def render_results():
    first_name = request.args.get("first", None)
    country = request.args.get("country", None)
    results = get_search_results(first_name=first_name,
                                 country=country)
    return render_template("results.html", data=results)


##################################
# Handle the individual profiles #
##################################

@app.route('/student/<int:sid>')
def get_student_profile(sid):
    return render_template("profile.html", sid=sid)

