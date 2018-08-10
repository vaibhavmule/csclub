from django.shortcuts import render, get_object_or_404
from django.contrib.syndication.views import Feed
from django.contrib.sitemaps import Sitemap
from django.urls import reverse

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


class LatestJobsFeed(Feed):
    title = "CSClub JobBoard"
    link = "/job/"
    description = "CS Trainee Vacancy and CS Jobs"

    def items(self):
        return Job.objects.all().order_by('-date_posted')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description

    def item_link(self, item):
        return reverse('job_detail', args=[item.slug])


class JobSitemap(Sitemap):
    def items(self):
        return Job.objects.all().order_by('-date_posted')

    def lastmod(self, obj):
        return obj.date_posted
