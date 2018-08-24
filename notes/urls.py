from django.urls import path
from notes.views import notes

urlpatterns = [
    path('', notes, name='notes'),
]
