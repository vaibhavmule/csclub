from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


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
        self.slug = slugify(self.title + ' at ' + self.employer.title)
        super(Job, self).save(*args, **kwargs)


class EmploymentType(BaseModel):
    title = models.CharField(max_length=50)
    value = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(EmploymentType, self).save(*args, **kwargs)


class Employer(BaseModel):
    title = models.CharField(max_length=150)
    website = models.URLField(null=True, blank=True)
    logo = models.ImageField(
        upload_to='logo/', default='/logo/default.jpg')

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ("title", "website")


class AddJobLog(BaseModel):
    last_modified = models.DateTimeField()
    etag = models.CharField(max_length=50)
    content_length = models.IntegerField()
    is_downloaded = models.BooleanField(default=False)

    def __str__(self):
        return str(self.content_length)