from django.urls import path
from page.views import home

urlpatterns = [
    path('', home, name='home'),
]
