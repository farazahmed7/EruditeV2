from __future__ import unicode_literals

from __future__ import unicode_literals
from django.db import models


class Stream(models.Model):
    stream = models.CharField(max_length=40)
    def __str__(self):
        return self.stream



class SemesterCS(models.Model):
    str=models.ForeignKey(Stream,on_delete=models.CASCADE)
    sem=models.CharField(max_length=30)
    def __str__(self):
        return self.sem

class SemesterECE(models.Model):
    str=models.ForeignKey(Stream,on_delete=models.CASCADE)
    sem=models.CharField(max_length=30)
    def __str__(self):
        return self.sem



class SubjectCS(models.Model):
    subs=models.CharField(max_length=30)
    semeCS=models.ForeignKey(SemesterCS,on_delete=models.CASCADE)
    link=models.CharField(max_length=50)
    def __str__(self):
        return self.subs

class SubjectECE(models.Model):
    subs=models.CharField(max_length=30)
    semeECE=models.ForeignKey(SemesterECE,on_delete=models.CASCADE)
    link=models.CharField(max_length=50)
    def __str__(self):
        return self.subs






