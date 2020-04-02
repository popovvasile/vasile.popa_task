"""
Define the REST verbs relative to the users
"""

from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument
from repositories import UserRepository

# create new user with contact data
# return user by id
# return user by name
# add additional mail/phone data
# update existing mail/phone data
# delete user
# from src.util import parse_params
from util import parse_params


class CreateUserResource(Resource):
    @staticmethod
    @parse_params(
        Argument("last_name", location="json", required=True, help="The last name of the user."),
        Argument("first_name", location="json", required=True, help="The first name of the user."),
        Argument("emails", location="json", required=False, help="The emails of the user."),
        Argument("phone_numbers", location="json", required=False, help="The phone_numbers of the user."),
    )
    @swag_from("../swagger/user/CREATE_USER.yml")
    def post(last_name, first_name, emails, phone_numbers):
        """ Create an user based on the sent information """
        user = UserRepository.create(
            last_name=last_name,
            first_name=first_name,
            emails=emails,
            phone_numbers=phone_numbers
        )
        return jsonify({"user": user.json})


class UserResource(Resource):
    """ Verbs relative to the users """

    @staticmethod
    @swag_from("../swagger/user/GET.yml")
    def get(user_id):
        """ Return an user key information based on his id """
        user = UserRepository.get(user_id=user_id)
        return jsonify({"user": user.json})

    @staticmethod
    @swag_from("../swagger/user/DELETE.yml")
    def delete(user_id):
        """ Delete an user based on his id """
        user = UserRepository.get(user_id=user_id)
        return jsonify({"user": user.json})

    @staticmethod
    @parse_params(
        Argument("emails", location="json", required=False,
                 help="The emails of the user."),
        Argument("phone_numbers", location="json", required=False,
                 help="The phone_numbers of the user."),
    )
    @swag_from("../swagger/user/POST.yml")
    def post(user_id, emails=None, phone_numbers=None):
        """ Add new emails or phone numbers """
        user = UserRepository().add(
            user_id=user_id,
            emails=emails,
            phone_numbers=phone_numbers
        )
        return jsonify({"user": user.json})

    @staticmethod
    @parse_params(
        Argument("last_name", location="json", required=False, help="The last name of the user."),
        Argument("first_name", location="json", required=False, help="The first name of the user."),
        Argument("emails", location="json", required=False, help="The emails of the user."),
        Argument("phone_numbers", location="json", required=False, help="The phone_numbers of the user."),
    )
    @swag_from("../swagger/user/PUT.yml")
    def put(user_id, last_name=None, first_name=None, emails=None, phone_numbers=None):
        """ Update an user based on the sent information """
        repository = UserRepository()
        user = repository.update(user_id=user_id,
                                 last_name=last_name, first_name=first_name,
                                 emails=emails, phone_numbers=phone_numbers)
        return jsonify({"user": user.json})
