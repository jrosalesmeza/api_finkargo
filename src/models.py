from app import db
from werkzeug.security import generate_password_hash,check_password_hash
from sqlalchemy import Column, Integer, String

class User(db.Model):

    __tablename__ = 'finkargo_user'

    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(80),nullable=False)
    email = db.Column(db.String(150),nullable=False, unique=True)
    password = db.Column(db.String(150),nullable=False)
    nationality_id= db.Column(db.Integer,  db.ForeignKey('finkargo_nationality.id'),nullable=False)
    nationality=db.relationship('Nationality',backref='finkargo_nationality')

    rol_id= db.Column(db.Integer,  db.ForeignKey('finkargo_rol.id'),nullable=False)
    rol = db.relationship('Rol', backref='finkargo_rol')

    def __init__(self,name,email,password,nationality_id,rol_id):
        self.name=name
        self.nationality_id=nationality_id
        self.password=generate_password_hash(password)
        self.email=email
        self.rol_id=rol_id

    def check_password(self, secret):
        return check_password_hash(self.password, secret)

    @property
    def serialize(self):
       return {
           "id": self.id,
           "name": self.name,
           "email": self.email,
           "nationality": self.nationality.serialize,
           "rol": self.rol.serialize
       }


class Nationality(db.Model):
    __tablename__ ='finkargo_nationality'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80),nullable=False, unique=True)
    code=db.Column(db.String(2),unique=True)

    def __init__(self,name,code):
        self.name=name
        self.code=code
    @property
    def serialize(self):
         return {
           "id": self.id,
           "name": self.name,
           "code": self.code,
       }

    
class Rol(db.Model):
    __tablename__ ='finkargo_rol'
    id = db.Column(db.Integer, primary_key=True)
    rol= db.Column(db.String(50),nullable=False,unique=True)
    def __init__(self,rol):
        self.rol=rol
    
    @property
    def serialize(self):
        return self.rol




