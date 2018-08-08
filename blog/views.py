from django.shortcuts import render, redirect
from blog.models import Post
from blog.forms import PostForm


def post(request):
    posts = Post.objects.filter(published_date__isnull=False)
    return render(request, 'blog_posts.html', {'posts': posts})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})


def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'post_detail.html', {'post': post})
