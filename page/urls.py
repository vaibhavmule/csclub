from django.urls import path
from page.views import home, about, privacy, contact

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('privacy/', privacy, name='privacy'),
    path('contact/', contact, name='contact'),
]
