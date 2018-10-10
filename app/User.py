""" User Model """

from config.database import Model


class User(Model):
    """User Model
    """

    __fillable__ = ['username', 'email', 'password']

    __auth__ = 'email'
