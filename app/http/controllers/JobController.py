"""A JobController Module"""

from slugify import slugify

from masonite.auth import Auth
from masonite.view import View
from masonite.request import Request

from app.Job import Job
from app.Employer import Employer
from app.EmploymentType import EmploymentType


class JobController:
    """JobController
    """

    def index(self, view: View, request: Request):
        jobs = Job.all()
        return view.render("job/index", {"jobs": jobs, 'app': request.app().make('Application')})

    def create(self, request: Request):
        employer = Employer.first_or_create(
            title=request.input('employer_title'),
            slug=slugify(request.input('employer_title')),
            website=request.input('employer_website')
        )

        employment_type = EmploymentType.find(1)

        job = Job(
            title=request.input('title'),
            description=request.input('description'),
            employer_id=employer.id,
            slug = '',
            employment_type_id=employment_type.id,
            location=request.input('location'),
            salary=request.input('salary'),
            apply_link=request.input('apply_link'),
            apply_email=request.input('apply_email'),
        )

        job.save()

        job.slug = slugify(request.input('title') + " " + str(job.id))

        job.save()

        return request.redirect('/')

    def new(self, view: View):
        return view.render('job/new')

    def show(self, view: View, request: Request):
        jobs = Job.where('slug', request.param('slug')).get()
        return view.render('job/show', {"job": jobs[0]})

    def companies(self, view: View):
        companies = Employer.all()
        return view.render('job/companies', {'companies': companies})

    def show_company(self, view: View, request: Request):
        employer = Employer.where('slug', request.param('slug')).get()[0]
        jobs = Job.where('employer_id', employer.id).get()
        return view.render('job/index', {'jobs': jobs, 'employer': employer})

        
