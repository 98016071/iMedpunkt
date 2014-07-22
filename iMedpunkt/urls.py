from django.conf.urls import patterns, url
from iMedpunkt.views import student_list, root

urlpatterns = patterns('',
    url(r'^student_list$', student_list, name='student_list'),
    url(r'^$', root, name='root')
)