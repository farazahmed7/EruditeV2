from django.contrib import admin
from .models import Stream,SemesterECE,SemesterCS,SubjectCS,SubjectECE


# Register your models here.

admin.site.register(Stream)
admin.site.register(SemesterCS)
admin.site.register(SubjectCS)
