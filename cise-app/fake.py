###################################
# Create database entries easily. #
##############################

# 1. Make a function to create a bogus entry.
# 2. Make many of those.
# 3. Do db.session.add() to all of those.
# 3. Do db.session.commit()

from faker import Faker
fake = Faker()
from cise.models import Student, Visa, Major, Note, Staff, Passport
import random

class DataGen:

    def __init__(self):
        self.seen_student_ids = set()
        self.seen_passport_ids = set()
        self.seen_visa_ids = set()
        self.seen_major_ids = set()
        self.seen_note_ids = set()

    def generate_id(self, seen_ids):
        i = 0
        while i < 100:
            num = fake.random_int(min=2, max=10000000, step=1)
            if num not in seen_ids:
                seen_ids.add(num)
                return num
        print("couldn't generate id")
        return None

    def create_specified_student(self, date_of_birth=None, preferred_name=None, legal_first=None,
                                legal_middle=None, legal_last=None, sex=None, class_year=None,
                                ac_email=None, sevis_id=None):
                                    if date_of_birth == None:
                                        date_of_birth = fake.
                                    return Student(sid=self.generate_id(self.seen_student_ids),
                                                    date_of_birth=date_of_birth,
                                                    preferred_name=preferred_name,
                                                    legal_first=legal_first,
                                                    legal_middle=legal_middle,
                                                    legal_last=legal_last,
                                                    sex=sex, class_year=class_year,
                                                    ac_email=ac_email, sevis_id=sevis_id)

    def create_student(self):
        return Student(sid=self.generate_id(self.seen_student_ids),
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

    def create_passport(self, sid):
        return Passport(number=self.generate_id(self.seen_passport_ids),
                        country=fake.country(),
                        date_of_issue=fake.date_this_decade(before_today=True),
                        date_of_expiration=fake.date_this_decade(),
                        student_sid=sid)

    def create_visa(self, sid):
        return Visa(visa_num=self.generate_id(self.seen_visa_ids),
                    date_of_issue=fake.date_this_decade(before_today=True),
                    date_of_expiration=fake.date_this_decade(),
                    visa_type="OPT",
                    file_path="test/file-path", student_sid=sid)

    def create_note(self, sid):
        return Note(note_id=self.generate_id(self.seen_note_ids),
                    date_created=fake.date_this_decade(before_today=True),
                    content=fake.sentence(), student_sid=sid)

    def create_major(self, sid):
        total_majors = Major.query.all()
        num_majors = random.randint(1,3)
        majors = []
        num_total_majors = len(total_majors)
        i = 0
        while i < num_majors:
            rand = random.randint(0,num_total_majors-1)
            choice = total_majors[rand]
            if choice in majors:
                continue
            else:
                majors.append(choice)
                i = i+1
        return majors;

    ''' 
    def create_major(self, sid):
        major_list = ('Math', 'Computer Science', 'Sports', 'Political Science',
                        'English', 'LLAS', 'Economics', 'Black Studies', 'LJST')
        major = fake.random_element(elements=major_list)
        return Major(cip_code=fake.lexify(text="???", letters='abcdefghijklmnopqrstuvwxyz'),
                     name=major, abbreviation=major[:3], student_sid=sid)
    ''' 
