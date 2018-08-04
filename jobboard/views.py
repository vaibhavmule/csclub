from django.shortcuts import render

from jobboard.models import Job


def jobs(request):
    jobs = Job.objects.all().order_by('-date_posted')
    return render(request, 'jobs.html', {'jobs': jobs})


def job_detail(request, id):
    job = Job.objects.get(id=id)
    return render(request, 'job_detail.html', {'job': job})
