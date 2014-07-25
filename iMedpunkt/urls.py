from django.conf.urls import patterns, url
from iMedpunkt.views import student_list, root, student, student_post, visits_list, visit_edit


urlpatterns = patterns('',
    url(r'^student/(?P<student_id>\d+)$', student, name='student'),
    url(r'^student_list$', student_list, name='student_list'),
    url(r'^student_post/(?P<student_id>\d+)$', student_post, name='student_post'),
    url(r'^visits_list$', visits_list, name='visits_list'),
    url(r'^visit_edit/(?P<student_id>\d+)$', visit_edit, name='visit_edit'),
    url(r'^$', root, name='root')
)