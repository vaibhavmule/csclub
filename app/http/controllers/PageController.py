""" A PageController Module """

from masonite.view import View
from masonite.request import Request
from app.Job import Job


class PageController:
    """PageController Controller
    """

    def index(self, view: View, request: Request):
        jobs = Job.all()
        return view.render("job/index", {"jobs": jobs, 'app': request.app().make('Application')})

    def about(self, view: View):
        return view.render('about')
    
    def privacy(self, view: View):
        return view.render('privacy')

    def contact(self, view: View):
        return view.render('contact')
