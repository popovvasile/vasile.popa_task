import json
import unittest

from models import User
from models.abc import db
from repositories import UserRepository
from server import server


class TestUser(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = server.test_client()

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get(self):
        """ The GET on `/user` should return an user """
        user = UserRepository.create(first_name="John", last_name="Doe",
                                     emails=["popovvasile@gmail.com"],
                                     phone_numbers=["+491424324435"])
        response = self.client.get("/application/user/{}".format(user.id))

        self.assertEqual(response.status_code, 200)
        response_json = json.loads(response.data.decode("utf-8"))
        self.assertEqual(
            response_json,
            {"user": dict(user_id=user.id,
                          first_name="John", last_name="Doe",
                          emails=["popovvasile@gmail.com"],
                          phone_numbers=["+491424324435"])},
        )

    def test_create(self):
        """ The POST on `/user` should create an user """
        response = self.client.post(
            "/application/user/Doe/John",
            content_type="application/json",
            data=json.dumps(dict(
                first_name="John", last_name="Doe",
                emails=["popovvasile@gmail.com"],
                phone_numbers=["+491424324435"])),
        )

        self.assertEqual(response.status_code, 200)
        response_json = json.loads(response.data.decode("utf-8"))
        self.assertEqual(
            response_json,
            {"user": dict(user_id=response_json["user"]["user_id"],
                          first_name="John", last_name="Doe",
                          emails=["popovvasile@gmail.com"],
                          phone_numbers=["+491424324435"])},
        )
        self.assertEqual(User.query.count(), 1)

    def test_update(self):
        """ The PUT on `/user` should update an user's info"""
        user = UserRepository.create(first_name="John", last_name="Doe")
        response = self.client.put(
            "/application/user/{}".format(user.id),
            content_type="application/json",
            data=json.dumps(dict(
                          first_name="John", last_name="Doe",
                          emails=["popovvasile@gmail.com"],
                          phone_numbers=["+491424324435"])),
        )

        self.assertEqual(response.status_code, 200)
        response_json = json.loads(response.data.decode("utf-8"))
        self.assertEqual(
            response_json,
            {"user": dict(user_id=user.id,
                          first_name="John", last_name="Doe",
                          emails=["popovvasile@gmail.com"],
                          phone_numbers=["+491424324435"])},
        )
        user = UserRepository.get(user_id=user.id)
        self.assertEqual(user.first_name, "John")
