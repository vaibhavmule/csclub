import requests
import pytz
import openpyxl

from datetime import datetime, timedelta

from django.core.management.base import BaseCommand
from jobboard.models import Job, Employer, EmploymentType, AddJobLog


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


def str_to_date(s):
    if s.startswith('Reposted on '):
        dt = datetime.strptime(
            s.replace('Reposted on ', ''), '%d-%m-%Y').date()
        print('dt', dt)
        return dt
    elif s.startswith('Re posted on '):
        dt = datetime.strptime(
            s.replace('Re posted on ', ''), '%d-%m-%Y').date()
        print('dt', dt)
        return dt
    elif s.startswith('Re-posted on '):
        dt = datetime.strptime(
            s.replace('Re-posted on ', ''), '%d-%m-%Y').date()
        print('dt', dt)
        return dt
    elif s.startswith('Resposted on '):
        dt = datetime.strptime(
            s.replace('Resposted on ', ''), '%d/%m/%Y').date()
        print('dt', dt)
        return dt
    else:
        # todo - email to me
        return datetime.strptime(s, '%d/%m/%Y').date()


def max_row(sheet):
    h_column = sheet['H']
    max_col = 2
    now = datetime.now() - timedelta(days=31)
    for col in h_column[2:20]:
        d = col.value

        # print(isinstance(d, datetime), d.date(), now.date())

        if isinstance(d, datetime) and d.date() >= now.date():
            max_col += 1
        elif isinstance(d, str) and str_to_date(d) and str_to_date(d) >= now.date():
            max_col += 1
        else:
            print(max_col)
            break

    return max_col


def is_latest_file():
    url = 'http://www.icsi.edu/Docs/Webmodules/Requirement.xlsx'
    r = requests.get(url)
    headers = r.headers

    latest = None
    if AddJobLog.objects.count():
        latest = AddJobLog.objects.latest('created')

    job_log = AddJobLog(
        etag=headers['ETag'].replace('"', ''),
        content_length=int(headers['Content-Length']),
        last_modified=datetime.strptime(
            headers['Last-Modified'],
            '%a, %d %b %Y %X %Z',
        ).astimezone(pytz.timezone('Asia/Kolkata')))
    job_log.save()
    is_latest = True
    if latest:
        etag = latest.etag == job_log.etag
        content_length = latest.content_length == job_log.content_length
        last_modified = latest.last_modified == job_log.last_modified
        is_downloaded = AddJobLog.objects.filter(
            etag=job_log.etag,
            content_length=job_log.content_length,
            last_modified=job_log.last_modified,
            is_downloaded=True).exists()
        if etag and content_length and last_modified and is_downloaded:
            is_latest = False
    return is_latest, job_log


def add_cs_trainee_job(row):
    """
    S.No.
    Company Name
    Address
    Email id
    Contact Person Name
    Requirement
    Location
    Posted on
    """
    d = row[7].value
    if isinstance(d, datetime):
        print('----------------------------------------\n')
        print("{} Looking for CS Trainees in {}".format(
            row[1].value, row[6].value),)
        html = "<strong>Requirement:</strong> {} <br/><strong>Address:</strong> {} <br/><strong>Contact Person:</strong> {}".format(
            row[5].value,
            row[2].value,
            row[4].value)
        print(html)
        date_posted = datetime.combine(
            d, datetime.now().time())
        employer = None
        if Employer.objects.filter(title=row[1].value).exists():
            employer = Employer.objects.get(title=row[1].value)
        else:
            employer = Employer.objects.create(title=row[1].value)
        job = Job(
            title="CS Trainee",
            description=html,
            employer=employer,
            location=row[6].value,
            date_posted=date_posted,
            apply_email=row[3].value)
        employment_type, created = EmploymentType.objects.get_or_create(
            title='Internship',
            value='INTERN',
        )
        job.save()
        job.employment_type.add(employment_type)
    else:
        print('----------------------------------------\n')
        print("{} Looking for CS Trainees in {}".format(
            row[1].value, row[6].value),)
        print("<strong>Company Name:</strong> {} <br/><strong>Requirement:</strong> {} <br/><strong>Address:</strong> {} <br/><strong>Location:</strong> {} <br/><strong>Email:</strong> {} <br/><strong>Contact Person:</strong> {} <br/><br/> <strong>Source:</strong> {} at <a href='https://www.icsi.edu/Docs/Webmodules/Requirement.xlsx'>ICSI</a>".format(
            row[1].value,
            row[5].value,
            row[2].value,
            row[6].value,
            row[3].value,
            row[4].value,
            row[7].value))


class Command(BaseCommand):
    help = 'Add jobs from ICSI'

    def handle(self, *args, **options):
        is_latest, job_log = is_latest_file()
        if is_latest:
            file_path = download_file()
            wb = openpyxl.load_workbook(file_path)
            sheet = wb.active
            mx_row = max_row(sheet)
            iter_rows = sheet.iter_rows(min_row=3, max_col=8, max_row=mx_row)
            if mx_row > 2:
                for row in iter_rows:
                    add_cs_trainee_job(tuple(row))
            job_log.is_downloaded = True
            job_log.save()
        self.stdout.write(self.style.SUCCESS('ok'))
