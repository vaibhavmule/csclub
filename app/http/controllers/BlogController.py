"""A BlogController Module"""

from slugify import slugify

from masonite.view import View
from masonite.request import Request
from app.Post import Post
from app.User import User


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
        post = Post.where(
            'slug', request.param('slug')).first_or_fail()
        return view.render('blog/show', {"post": post})

    def user_posts(self, view: View, request: Request):
        username = request.param('username')
        author = User.where('username', username).first_or_fail()
        if request.user().username == username:
            posts = Post.where('author_id', author.id).get()
        else:
            posts = Post.where('author_id', author.id).where_null('published_date').get()
            
        return view.render('blog/user_posts', {'posts': posts, 'author': author})

