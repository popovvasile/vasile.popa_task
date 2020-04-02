from sqlalchemy import Integer, Column, ForeignKey
from sqlalchemy.orm import relationship

from . import db
from .abc import BaseModel, MetaBaseModel


class User(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The User model """

    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    first_name = db.Column(db.String(300))
    last_name = db.Column(db.String(300))
    emails = relationship("Email")
    phone_numbers = relationship("PhoneNumber")

    def __init__(self, first_name, last_name, emails, phone_numbers):
        """ Create a new User """
        self.first_name = first_name
        self.last_name = last_name
        self.emails = emails
        self.phone_numbers = phone_numbers


class Email(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The Email model """

    __tablename__ = "email"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    mail = db.Column(db.String(300))

    def __init__(self, mail, user_id):
        """ Create a new Email """
        self.mail = mail
        self.user_id = user_id


class PhoneNumber(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The PhoneNumber model """

    __tablename__ = "phone_number"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    number = db.Column(db.String(300))

    def __init__(self, number, user_id):
        """ Create a new Email """
        self.number = number
        self.user_id = user_id
