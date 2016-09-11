from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^api/sem$', views.showSemesters, name='showSem'),
    url(r'^api/sub$', views.showSubjects, name='showSub'),


]