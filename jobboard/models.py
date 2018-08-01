from django.db import models


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Job(BaseModel):
    title = models.CharField(max_length=50)
    date_posted = models.DateTimeField(auto_now_add=True, editable=True)
    description = models.TextField()
    employment_type = models.ManyToManyField('EmploymentType')
    employer = models.ForeignKey('Employer', on_delete=models.PROTECT)
    location = models.CharField(max_length=150)
    expiry_date = models.DateTimeField()
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


class EmploymentType(BaseModel):
    title = models.CharField(max_length=50)
    value = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class Employer(BaseModel):
    title = models.CharField(max_length=150)
    website = models.URLField()
    logo = models.ImageField(upload_to='logo/')

    def __str__(self):
        return self.title
