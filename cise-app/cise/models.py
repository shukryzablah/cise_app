from sqlalchemy import Column, Integer, String, Date
from cise import db


class Example(db.Model):
    __tablename__ = 'example'
    id = Column(Integer, primary_key=True)
    text = Column(String)
    date_created = Column(Date)

    def __repr__(self):
        return "<Example(text='{}', date='{}')>"\
                .format(self.text, self.date_created)
