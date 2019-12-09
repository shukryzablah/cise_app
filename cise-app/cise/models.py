from sqlalchemy import Column, Integer, String, Date
from cise import db


class Example(db.Model):
    __tablename__ = 'example'
    eid = Column(Integer, primary_key=True)
    text = Column(String)
    date_created = Column(Date)

    def __repr__(self):
        return "<Example(text='{}', date='{}')>"\
                .format(self.text, self.date_created)


class Student(db.Model):
    __tablename__ = 'student'
    sid = Column(Integer, primary_key=True)
    date_of_birth = Column(Date)
    preferred_name = Column(String)
    legal_first = Column(String)
    legal_middle = Column(String)
    legal_last = Column(String)
    sex = Column(String)
    class_year = Column(Integer)
    ac_box = Column(String)
    ac_email = Column(String)
    sevis_id = Column(String)
    sevis_status = Column(String)
    program_start_date = Column(Date)
    program_end_date = Column(Date)

    passport_id = db.relationship('Passport', backref='student', lazy=True)

    def __repr__(self):
        return "<Student(sid={}, class_year={})>".format(self.sid,
                                                         self.class_year)
    def serialize(self):
        passport_list = [passport.serialize() for passport in self.passport_id]
        return {
            'sid': self.sid,
            'legal_first': self.legal_first,
            'legal_last': self.legal_last,
            'passport_id': passport_list
        }
       
class Visa(db.Model):
    __tablename__ = 'Visa'
    visa_num = Column(Integer, primary_key=True)
    date_of_issue = Column(Date)
    date_of_expiration = Column(Date)
    visa_type = Column(String)
    file_path = Column(String)

    def __repr__(self):
        return "<Visa(visa_num={})>".format(self.visa_num)

    def serialize(self):
        return {
            'visa_num': self.visa_num,
            'date_of_issue': self.date_of_issue,
            'date_of_expiry': self.date_of_expiration,
            'file_path': self.file_path
        }
 
            
class Major(db.Model):
    __tablename__ = 'major'
    cip_code = Column(String, primary_key=True)
    name = Column(String)
    abbreviation = Column(String)

    def __repr__(self):
        return "<Major(cip_code={}, name={})>".format(self.cip_code,
                                                      self.name)


class Passport(db.Model):
    __tablename__ = 'passport'
    number = Column(String, primary_key=True)
    country = Column(String)
    date_of_issue = Column(Date)
    date_of_expiration = Column(Date)
    student_sid = db.Column(Integer, db.ForeignKey('student.sid'))

    def __repr__(self):
        return "<Passport(number={}, country={})>".format(self.number,
                                                          self.country)

    def serialize(self):
        return {
            'number': self.number,
            'country': self.country,
            'date_of_expiration': self.date_of_expiration,
            'student_sid': self.student_sid
        }
