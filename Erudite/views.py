from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from .models import Stream,SemesterECE,SemesterCS,SubjectCS,SubjectECE
from .serializers import SemesterSerializer, SubjectSerializer
from rest_framework.response import Response



# Create your views here.

@csrf_exempt
@api_view(['GET', 'POST', ])
def showSemesters(request):
    if request.method=="POST":
        _stream=str(request.POST['stream'])
        s=Stream.objects.get(stream=_stream)
        if _stream=="B.Tech CS":
           a=s.semestercs_set.all()
           ser=SemesterSerializer(a,many=True)
           return Response(ser.data)
        elif _stream=="B.Tech ECE":
            a=s.semesterece_set.all()
            ser=SemesterSerializer(a,many=True)
            return Response(ser.data)
    return HttpResponse("faraz")

@csrf_exempt
@api_view(['GET', 'POST', ])
def showSubjects(request):
    if request.method=="POST":
        _stream=request.POST['stream']
        _sem=request.POST['sem']
        s=Stream.objects.get(stream=_stream)

        if _stream=="B.Tech CS":
            a=s.semestercs_set.get(sem=_sem)
            x=a.subjectcs_set.all()
            ser=SubjectSerializer(x,many=True)
            return Response(ser.data)

        elif _stream=="B.Tech ECE":
            a=s.semesterece_set.get(sem=_sem)
            x=a.subjectece_set.all()
            ser=SubjectSerializer(x,many=True)
            return Response(ser.data)


