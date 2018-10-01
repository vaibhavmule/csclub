''' A Employer Database Model '''
from config.database import Model


class Employer(Model):
    __fillable__ = ['title', 'slug', 'website', 'logo']
