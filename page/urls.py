from django.urls import path
from page.views import home, about, privacy, contact, home_files

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('privacy/', privacy, name='privacy'),
    path('contact/', contact, name='contact'),
    path('<filename>', home_files, name='home_files'),
]