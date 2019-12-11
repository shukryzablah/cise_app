from cise import app
from cise.models import *
from flask import jsonify, request, redirect, url_for, render_template, json


############
# Homepage #
############

@app.route('/')
def render_home():
    countries = Passport.query.with_entities(Passport.country).distinct().order_by(Passport.country).all()
    countries = [country[0] for country in countries]
    return render_template("home.html", data=countries)

@app.route('/search', methods=['POST'])
def handle_search_request():
    return redirect(
        url_for("render_results", **request.form, _method="GET")
    )

###########
# Results #
###########

def get_search_results(**kwargs):
    # First get possible values to filter by.
    first_name = kwargs.pop("first_name", None)
    last_name = kwargs.pop("last_name", None)
    country = kwargs.pop("country", None)
    # Then construct the appropriate query by filtering.
    query = Student.query.join(Student.passport_id)
    if(first_name is not None and first_name != ""):
        query = query.filter(Student.legal_first == first_name)
    if(last_name is not None and last_name != ""):
        query = query.filter(Passport.legal_last == last_name)
    if(country is not None and country != ""):
        query = query.filter(Passport.country == country)
   # if(major is not None and major != ""):
    #    query = query.filter(Passport. == country)
    # Execute the query and return response.
    results = query.all()
    return json.dumps([result.serialize() for result in results])

@app.route('/')
def render_home():
    countries = Passport.query.with_entities(Passport.country).distinct().order_by(Passport.country).all()
    countries = [country[0] for country in countries]

    majors = []

    # majors = Student.query.with_entities(Student.major).distinct().order_by(Student.major).all()
    # majors = [country[0] for country in countries]
    return render_template("home.html", countries=countries, majors=majors)


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

@app.route('/search-results')
def render_results():
    # Get arguments from form for clarity
    first_name = request.args.get("first", None)
    last_name = request.args.get("last", None)
    country = request.args.get("country", None)
    major = request.args.get("major", None)
    # Pass arguments to helper function for filtering.
    results = get_search_results(first_name=first_name,
                                 last_name=last_name,
                                 country=country,
                                 major=major)
    return render_template("results.html", data=results)


##################################
# Handle the individual profiles #
##################################

@app.route('/student/<int:sid>')
def get_student_profile(sid):
    # join on all info
    student = Student.query.filter(Student.sid == sid).all()
    return render_template("profile.html", student=student)


#########
# Other #
#########

@app.route('/get-student-passport')
def get_student_passport():
    join = Student.query.join(Passport).first()
    return jsonify(join.serialize())

