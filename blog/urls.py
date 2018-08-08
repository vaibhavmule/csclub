from django.urls import path
from blog.views import post, post_detail, post_new

urlpatterns = [
    path('', post, name='post'),
    path('new/', post_new, name='post_new'),
    path('<slug:slug>/', post_detail, name='post_detail'),
]
