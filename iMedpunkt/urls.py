from django.conf.urls import patterns, url
from iMedpunkt.views import student_list, root, student, student_post, visits_list, visit_edit, visit_post, visit_new, login, \
date_edit

urlpatterns = patterns('',
    url(r'^student/(?P<student_id>\d+)$', student, name='student'),
    url(r'^student_list$', student_list, name='student_list'),
    url(r'^student_post/(?P<student_id>\d+)$', student_post, name='student_post'),
    url(r'^visits_list$', visits_list, name='visits_list'),
    url(r'^visit_edit/(?P<visit_id>\d+)$', visit_edit, name='visit_edit'),
    url(r'^visit_post/(?P<visit_id>\d+)$', visit_post, name='visit_post'),
    url(r'^visit_new/(?P<student_id>\d+)$', visit_new, name='visit_new'),
    url(r'^date_edit/(?P<visit_id>\d+)$', date_edit, name='date_edit'),
    url(r'^$', root, name='root')
)