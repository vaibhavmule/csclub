""" A BlogController Module """

from masonite.view import View


class BlogController:
    """BlogController Controller
    """

    def index(self, view: View):
        return view.render('blog/index')
