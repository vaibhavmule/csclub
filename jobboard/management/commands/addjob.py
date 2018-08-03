import requests

from django.core.management.base import BaseCommand
from jobboard.models import Job


def download_file():
    url = 'http://www.icsi.edu/Docs/Webmodules/Requirement.xlsx'
    local_filename = '/tmp/' + url.split('/')[-1]
    print('Downloading File...', local_filename)
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    print('Downloaded')
    return local_filename


class Command(BaseCommand):
    help = 'Add jobs from ICSI'

    def handle(self, *args, **options):
            self.stdout.write(self.style.SUCCESS())
