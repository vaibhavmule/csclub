''' A Job Database Model '''
from config.database import Model
from orator.orm import belongs_to


class Job(Model):
    __fillable__ = ['title', 'slug', 'date_posted', 'description', 'location', 'expiry_date', 'salary', 'salary_unit', 'apply_link', 'apply_email', 'employer_id', 'employment_type_id']

    @belongs_to('employer_id', 'id')
    def employer(self):
        from app.Employer import Employer
        return Employer

    @belongs_to('employment_type_id', 'id')
    def employment_type(self):
        from app.EmployerType import EmployerType
        return EmployerType
