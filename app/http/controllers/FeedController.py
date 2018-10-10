"""A FeedController Module"""

from masonite.view import View
from masonite.request import Request

from app.Post import Post


class FeedController:
    """FeedController
    """

    def blog(self, view: View, request: Request):
        posts = Post.all()
        request.header('Content-Type', 'application/xml', http_prefix=None)
        return view.render('feed/blog.xml', {'posts': posts})
