from django.urls import path
from blog.views import post, post_new, post_edit, LatestArtcileFeed

urlpatterns = [
    path('', post, name='post'),
    path('feed/', LatestArtcileFeed(), name='blog_feed'),
    path('new/', post_new, name='post_new'),
    path('<int:pk>/edit/', post_edit, name='post_edit'),
]
