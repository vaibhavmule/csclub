""" A JobController Module """

from masonite.view import View
from masonite.request import Request
from app.Job import Job

class JobController:
    """JobController Controller
    """

    def index(self, view: View, request: Request):
        jobs = Job.all()
        print(len(jobs))
        return view.render("index", {"jobs": jobs, 'app': request.app().make('Application')})

    def create(self, request: Request):
        Job.create(
            title=request.input('title'),
            description=request.input('description'),
            slug=request.input('title'),
            location=request.input('location'),
            salary=request.input('salary'),
            apply_link=request.input('apply_link'),
            apply_email=request.input('apply_email'),
        )

        return request.redirect('/')

    def new(self, view: View):
        return view.render('new')

