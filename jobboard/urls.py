from django.urls import path
from jobboard.views import jobs, job_detail, LatestJobsFeed

urlpatterns = [
    path('', jobs, name='jobs'),
    path('feed/', LatestJobsFeed(), name='job_feed'),
    path('<slug:slug>/', job_detail, name='job_detail')
]
