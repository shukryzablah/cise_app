from cise import app
from cise.models import *
from flask import jsonify, request, redirect, url_for, render_template, json

from datetime import date

from cise import db
from fake import DataGen

dg = DataGen()

############
# Homepage #
############

@app.route('/')
def render_home():
    countries = Passport.query.with_entities(Passport.country).distinct().order_by(Passport.country).all()
    countries = [country[0] for country in countries]
    majors = Major.query.with_entities(Major.name).distinct().order_by(Major.name).all()
    majors = [major[0] for major in majors]
    return render_template("home.html", countries=countries, majors=majors)

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
    major = kwargs.pop("major", None)
    # Then construct the appropriate query by filtering.
    #query = Student.query.join(Student.passport_id)
    query = Student.query
    if(first_name is not None and first_name != ""):
        query = query.filter(Student.legal_first.ilike(first_name))
    if(last_name is not None and last_name != ""):
        query = query.filter(Student.legal_last.ilike(last_name))
    if(country is not None and country != ""):
        query = query.join(Student.passport_id)
        query = query.filter(Passport.country.ilike(country))
    if(major is not None and major != ""):
        query = query.join(has_major).join(Major)
        query = query.filter(Major.name.ilike(major))
    # Execute the query and return response.
    results = query.all()
    return json.dumps([result.serialize() for result in results])


###########
# Results #
###########


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
    # student = student.join(Student.passport_id).join(Student.visa_id).join(Student.note_id).join(Student.majors)
    data = json.dumps([student.serialize_full() for student in student])
    return render_template("profile.html", data=data, sid=sid)


@app.route('/add-note/<int:sid>', methods=['POST'])
def handle_note_creation(sid):
    # Add note to student in database
    s = Student.query.filter(Student.sid == sid).first()
    n = Note(date_created=date.today(),
             content=request.form.get("notecontent"))
    db.session.add(n)
    db.session.commit()
    s.note_id.append(n)
    db.session.add(s)
    db.session.commit()
    return redirect(
        url_for("get_student_profile", sid=sid, _method="GET")
    )


################
# Add students #
################

@app.route('/add')
def add_page():
    return render_template("add.html")

@app.route('/added_student', methods=['POST'])
def add_student():
    first = request.args.get('first')
    last = request.args.get('last')
    country = request.args.get('country')
    major = request.args.get('major')
    class_year = request.args.get('class_year')
    ac_email = request.args.get('ac_email')
    stu, pport, major = dg.create_specified_student(legal_first=first, legal_last=last, country=country,
                                    major=major, class_year=class_year, ac_email=ac_email)
    data = []
    data.append(json.dumps(stu.serialize_full()))
    data.append(json.dumps(pport.serialize()))
    data.append(json.dumps(major.serialize()))
    return render_template("added.html", data=data)


#########
# Other #
#########

@app.route('/get-student-passport')
def get_student_passport():
    join = Student.query.join(Passport).first()
    return jsonify(join.serialize())

