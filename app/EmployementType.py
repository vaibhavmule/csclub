''' A EmployementType Database Model '''
from config.database import Model


class EmployementType(Model):
    __fillable__ = ['title', 'slug', 'value']
