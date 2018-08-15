from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.syndication.views import Feed
from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from blog.models import Post
from blog.forms import PostForm


def post(request):
    posts = Post.objects.filter(
        published_date__isnull=False).order_by('-published_date')
    return render(request, 'blog_posts.html', {'posts': posts})


def post_by_user(request, username):
    author = get_object_or_404(User, username=username)
    if request.user.username == username:
        posts = Post.objects.filter(
            author=author).order_by('-published_date')
    else:
        posts = Post.objects.filter(
            author__username=author,
            published_date__isnull=False).order_by('-published_date')
    return render(request,
                  'blog_posts_by_user.html',
                  {'posts': posts, 'author': author})


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect(
                'post_detail', username=post.author.username, slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})


@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect(
                'post_detail', username=post.author.username, slug=post.slug)
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})


def post_detail(request, username, slug):
    author = get_object_or_404(User, username=username)
    post = get_object_or_404(Post, slug=slug, author=author)
    return render(request, 'post_detail.html', {'post': post})


class LatestArtcileFeed(Feed):
    title = "CSClub Blog"
    link = "/blog/"
    description = "Stay updated about Company Secretary"

    def items(self):
        return Post.objects.filter(
            published_date__isnull=False).order_by('-published_date')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text

    def item_link(self, item):
        return reverse('post_detail', args=[item.author.username, item.slug])


class BlogSitemap(Sitemap):
    def items(self):
        return Post.objects.filter(
            published_date__isnull=False).order_by('-published_date')

    def lastmod(self, obj):
        return obj.published_date
