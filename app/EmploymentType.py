''' A EmploymentType Database Model '''
from config.database import Model


class EmploymentType(Model):
    __fillable__ = ['title', 'slug', 'value']
