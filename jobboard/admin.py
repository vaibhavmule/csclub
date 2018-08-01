from django.contrib import admin

from jobboard.models import Employer, EmploymentType, Job


admin.site.register(Employer)
admin.site.register(EmploymentType)
admin.site.register(Job)
