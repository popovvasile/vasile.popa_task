"""
Defines the blueprint for the users
"""
from flask import Blueprint
from flask_restful import Api

from resources import UserResource, CreateUserResource

USER_BLUEPRINT = Blueprint("user", __name__)
Api(USER_BLUEPRINT).add_resource(
    UserResource, "/user/<int:user_id>"
)
Api(USER_BLUEPRINT).add_resource(
    CreateUserResource, "/users/"
)
