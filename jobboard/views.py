from django.shortcuts import render, get_object_or_404

from jobboard.models import Job, Employer


def jobs(request):
    jobs = Job.objects.all().order_by('-date_posted')
    return render(request, 'jobs.html', {'jobs': jobs})


def job_detail(request, slug):
    job = Job.objects.get(slug=slug)
    return render(request, 'job_detail.html', {'job': job})


def jobs_by_employer(request, slug):
    employer = get_object_or_404(Employer, slug=slug)
    jobs = Job.objects.filter(employer=employer).order_by('-date_posted')
    return render(request, 'jobs.html', {'jobs': jobs, 'employer': employer})


def companies(request):
    companies = Employer.objects.all()
    return render(request, 'companies.html', {'companies': companies})
