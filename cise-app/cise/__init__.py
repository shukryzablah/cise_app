import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)

##################################
# retrieve environment variables #
##################################


def get_env_variable(name):
    try:
        return os.environ[name]
    except KeyError:
        message = f"Expected environment variable '{name}' not set."
        raise Exception(message)


POSTGRES_URL = get_env_variable("POSTGRES_URL")
POSTGRES_USER = get_env_variable("POSTGRES_USER")
POSTGRES_PW = get_env_variable("POSTGRES_PW")
POSTGRES_DB = get_env_variable("POSTGRES_DB")

#######################
# connect to database #
#######################

DB_URL = (
    f"postgresql+psycopg2://"
    f"{POSTGRES_USER}:{POSTGRES_PW}"
    f"@{POSTGRES_URL}/{POSTGRES_DB}"
)

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

###################
# retrieve models #
###################

from cise.models import Example, Student, Major, Passport, Note, Visa
#from cise.models import Example
######################
# retrieve app views #
######################

import cise.views

###################################
# add automatic imports for shell #
###################################

@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, Example=Example, Student=Student,
                Major=Major, Passport=Passport, Note=Note, Visa=Visa)


