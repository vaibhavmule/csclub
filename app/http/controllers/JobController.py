""" A JobController Module """

from slugify import slugify

from masonite.view import View
from masonite.request import Request

from app.Job import Job
from app.Employer import Employer
from app.EmploymentType import EmploymentType


class JobController:
    """JobController Controller
    """

    def index(self, view: View, request: Request):
        jobs = Job.all()
        print(len(jobs))
        for job in jobs:
            print(job.employment_type.all())
        return view.render("index", {"jobs": jobs, 'app': request.app().make('Application')})

    def create(self, request: Request):
        employer = Employer.first_or_create(
            title=request.input('employer_title'),
            slug=slugify(request.input('employer_title')),
            website=request.input('employer_website')
        )

        employment_type = EmploymentType.create(
            title="Internship",
            slug="internship",
            value="INTERNSHIP"
        )

        Job.create(
            title=request.input('title'),
            description=request.input('description'),
            slug=slugify(request.input('title')),
            employer_id=employer.id,
            employment_type_id=employment_type.id,
            location=request.input('location'),
            salary=request.input('salary'),
            apply_link=request.input('apply_link'),
            apply_email=request.input('apply_email'),
        )

        return request.redirect('/')

    def new(self, view: View):
        return view.render('new')

