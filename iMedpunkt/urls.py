from django.conf.urls import patterns, url
from iMedpunkt.views import student_list, root, student

urlpatterns = patterns('',
    url(r'^student/(?P<student_id>\d+)$', student, name='student'),
    url(r'^student_list$', student_list, name='student_list'),
    url(r'^$', root, name='root')
)