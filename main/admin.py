from django.contrib import admin
from .models import *
from employer.models import Employer,Job
# Register your models here.
admin.site.register(Employee)
admin.site.register(Employer) 
admin.site.register(Job)
admin.site.register(Jobstatus)