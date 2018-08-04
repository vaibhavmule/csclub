from django.shortcuts import render
from jobboard.models import Job


def home(request):
    jobs = Job.objects.all().order_by('-date_posted')
    return render(request, 'index.html', {'jobs': jobs})


def about(request):
    return render(request, 'about.html', {})


def privacy(request):
    return render(request, 'privacy.html', {})
