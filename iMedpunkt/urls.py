from django.conf.urls import patterns, url
from iMedpunkt.views import hello1, root

urlpatterns = patterns('',
    url(r'^hello$', hello1, name='hello'),
    url(r'^$', root, name='root')
)