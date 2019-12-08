###################################
# Create database entries easily. #
###################################

# 1. Make a function to create a bogus entry.
# 2. Make many of those.
# 3. Do db.session.add() to all of those.
# 3. Do db.session.commit()

from faker import Faker
fake = Faker()

def create_student():
    return Student(sid=fake.random_int(min=2, max=1000000,step=1),
                   date_of_birth=fake.date_of_birth(),
                   preferred_name=fake.first_name(),
                   legal_first=fake.first_name(),
                   legal_middle=fake.first_name(),
                   legal_last=fake.last_name(),
                   sex="Male",class_year=fake.year(),
                   ac_email=fake.email(),
                   sevis_id=fake.random_int(min=1,max=10000000,step=1),
                   sevis_status="active",
                   program_start_date=fake.date_this_decade(after_today=True),
                   program_end_date=fake.date_this_decade(after_today=True)
    )

def create_passport(sid):
    return Passport(number=fake.hexify(text="^^^^^^", upper=True),
                    country=fake.country(),
                    date_of_issue=fake.date_this_decade(before_today=True),
                    date_of_expiration=fake.date_this_decade(),
                    student_sid=sid)
