from django.contrib import admin

# Register your models here.
from iMedpunkt.models import Student, Visit

admin.site.register(Student)
admin.site.register(Visit)