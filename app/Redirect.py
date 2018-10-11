""" Redirect Model """

from config.database import Model


class Redirect(Model):
    """Redirect Model
    """
    __fillable__ = ['old_path', 'new_path']