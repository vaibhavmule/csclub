from django.urls import path
from jobboard.views import jobs, job_detail

urlpatterns = [
    path('', jobs, name='jobs'),
    path('<int:id>', job_detail, name='job_detail'),
]
