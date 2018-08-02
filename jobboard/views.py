from django.shortcuts import render

from jobboard.models import Job


def jobs(request):
    jobs = Job.objects.all()
    return render(request, 'jobs.html', {'jobs': jobs})


def job_detail(request, id):
    job = Job.objects.get(id=id)
    return render(request, 'job_detail.html', {'job': job})
