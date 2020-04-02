""" Defines the User repository """

from models import User, Email, PhoneNumber


class UserRepository:
    """ The repository for the user model """

    @staticmethod
    def get(user_id):
        """ Query a user by user_id"""
        return User.query.filter_by(id=user_id).one()

    def update(self, user_id, last_name=None, first_name=None, emails=None, phone_numbers=None):
        """ Update a user's info """
        user = self.get(user_id)
        if last_name:
            user.last_name = last_name
        if first_name:
            user.first_name = first_name

        if emails:
            old_emails = Email.query.filter_by(id=user_id).all()
            for old_email in old_emails:
                old_email.delete()
            self.add(user_id, emails=emails)

        if phone_numbers:
            old_numbers = PhoneNumber.query.filter_by(id=user_id).all()
            for old_number in old_numbers:
                old_number.delete()
            self.add(user_id, phone_numbers=phone_numbers)

        return user.save()

    def add(self, user_id, emails=None, phone_numbers=None):
        """ Add emails or phone numbers"""
        user = self.get(user_id)

        if emails:
            for mail in emails:
                email_obj = Email.query.filter_by(id=user_id).one()
                email_obj.mail = mail
                email_obj.save()
        if phone_numbers:
            for number in phone_numbers:
                number_obj = PhoneNumber.query.filter_by(id=user_id).one()
                number_obj.number = number
                number_obj.save()
        return user.save()

    @staticmethod
    def create(last_name, first_name, emails=None, phone_numbers=None):
        """ Create a new user """
        user = User(last_name=last_name, first_name=first_name)
        if emails:
            for email in emails:
                Email(mail=email, user_id=user.id).save()
        if phone_numbers:
            for number in phone_numbers:
                PhoneNumber(number=number, user_id=user.id).save()
        return user.save()

    def delete(self, user_id):
        """ Delete a user """
        user = self.get(user_id).delete()

        return user
