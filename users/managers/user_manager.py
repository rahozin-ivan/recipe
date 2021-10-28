from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, email, password, **kwargs):
        """Creates and saves a new user"""
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()

        return user
