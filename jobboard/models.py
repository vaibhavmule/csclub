import json

from django.contrib.sites.models import Site
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify


from csclub.models import BaseModel


def from_now_30_days():
    return timezone.now() + timezone.timedelta(days=30)


class Job(BaseModel):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    date_posted = models.DateTimeField(auto_now_add=True, editable=True)
    description = models.TextField()
    employment_type = models.ManyToManyField('EmploymentType')
    employer = models.ForeignKey('Employer', on_delete=models.PROTECT)
    location = models.CharField(max_length=150)
    expiry_date = models.DateTimeField(default=from_now_30_days)
    salary = models.DecimalField(max_digits=7, decimal_places=2, default=0.00)
    UNIT_CHOICES = (
        ('M', 'Month'),
        ('Y', 'Year'),
    )
    salary_unit = models.CharField(
        max_length=2,
        choices=UNIT_CHOICES,
        default='M',
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title + ' ' + str(self.id))
        super(Job, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('job_detail', kwargs={'slug': self.slug})

    def json_ld(self):
        return json.dumps({
            '@context': 'http://schema.org/',
            '@type': "JobPosting",
            'datePosted': self.date_posted.isoformat(),
            'title': self.title,
            'description': self.description,
            'validThrough': self.expiry_date.isoformat(),
            'employmentType': list(
                self.employment_type.values_list('value', flat=True)),
            'jobLocation': {'@type': 'Place', 'address': 'Mumbai'},
            'hiringOrganization': self.employer.json_ld(),
            'baseSalary': {
                '@type': 'MonetaryAmount',
                'currency': 'INR',
                'value': {
                    '@type': 'QuantitativeValue',
                    'value': str(self.salary),
                    'unitText': self.get_salary_unit_display()
                }
            },
            'identifier': {
                '@type': 'PropertyValue',
                'name': self.employer.title,
                "value": 'http://{}{}'.format(
                    Site.objects.get_current().domain,
                    self.get_absolute_url())
            },
        })


class EmploymentType(BaseModel):
    title = models.CharField(max_length=100)
    value = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(EmploymentType, self).save(*args, **kwargs)


class Employer(BaseModel):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, max_length=150)
    website = models.URLField(null=True, blank=True)
    logo = models.ImageField(
        upload_to='logo/', default='/logo/default.jpg')

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ("title", "website")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Employer, self).save(*args, **kwargs)

    def json_ld(self):
        return {
            '@type': 'Organization',
            'name': self.title,
            "sameAs": self.website,
            "url": self.website,
            "logo": self.logo.url,
        }


class AddJobLog(BaseModel):
    last_modified = models.DateTimeField()
    etag = models.CharField(max_length=50)
    content_length = models.IntegerField()
    is_downloaded = models.BooleanField(default=False)

    def __str__(self):
        return str(self.content_length)
