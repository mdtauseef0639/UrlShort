import string
from datetime import datetime
from random import choices
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class ShortenLink(db.Model):
    __tablename__ = 'url__code__table'
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(512))
    code_ = db.Column(db.String(4), unique=True)
    date_created = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.code = self.generate()

    def generate(self):
        characters = string.digits + string.ascii_letters
        code = ''.join(choices(characters, k=4))

        link = self.query.filter_by(code_=code).first()

        if link:
            return self.generate()

        return code
