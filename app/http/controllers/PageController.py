""" A PageController Module """

from masonite.view import View
from masonite.request import Request
from app.Job import Job


class PageController:
    """PageController Controller
    """

    def index(self, view: View, request: Request):
        jobs = Job.all()
        print(len(jobs))
        return view.render("index", {"jobs": jobs, 'app': request.app().make('Application')})
