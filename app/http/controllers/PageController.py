""" A PageController Module """

from masonite.view import View


class PageController:
    """PageController Controller
    """

    def index(self, view: View):
        return view.render('index')
