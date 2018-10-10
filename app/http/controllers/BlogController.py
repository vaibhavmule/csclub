"""A BlogController Module"""

from slugify import slugify

from masonite.view import View
from masonite.request import Request
from app.Post import Post


class BlogController:
    """BlogController
    """

    def index(self, view: View):
        posts = Post.all()
        return view.render('blog/index', {'posts': posts})

    def new(self, view: View):
        return view.render('blog/new')

    def create(self, request: Request):

        post = Post(
            title=request.input('title'),
            text=request.input('text'),
            author_id=request.user().id,
            slug = '',
        )

        post.save()

        post.slug = slugify(request.input('title')),

        post.save()

        return request.redirect('/blog')

    def show(self, view: View, request: Request):
        posts = Post.where(
            'slug', request.param('slug')).get()
        return view.render('blog/show', {"post": posts[0]})
    
