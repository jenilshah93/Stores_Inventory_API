import sqlite3
from db import dba
class UserModel(dba.Model):
    __tablename__='users'

    id = dba.Column(dba.Integer,primary_key = True)
    username = dba.Column(dba.String(80))
    password = dba.Column(dba.String(80))
    def __init__(self,username,password):
        self.username = username
        self.password = password
    def save_to_db(self):
        dba.session.add(self)
        dba.session.commit()
    @classmethod
    def find_by_username(cls,username):
        return cls.query.filter_by(username=username).first()
    @classmethod
    def find_by_id(cls,_id):
        return cls.query.filter_by(id=_id).first()
