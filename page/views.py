from django.shortcuts import render


from jobboard.models import Job


def home(request):
    jobs = Job.objects.all().order_by('-date_posted')
    return render(request, 'jobs.html', {'jobs': jobs})


def about(request):
    return render(request, 'about.html')


def privacy(request):
    return render(request, 'privacy.html')


def contact(request):
    return render(request, 'contact.html')


def home_files(request, filename):
    if filename in ['OneSignalSDKUpdaterWorker.js', 'OneSignalSDKWorker.js']:
        return render(request, filename, content_type="text/javascript")
    if filename == 'manifest.json':
        return render(request, filename, content_type="text/json")
    return render(request, filename, content_type="text/plain")
