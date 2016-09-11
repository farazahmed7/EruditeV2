from .models import Stream,SemesterECE,SemesterCS,SubjectCS,SubjectECE
from rest_framework import serializers

class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model=SemesterCS
        fields=('sem',)

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=SubjectCS
        fields=('subs','link')


