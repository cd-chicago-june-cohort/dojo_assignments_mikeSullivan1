
from django.conf.urls import url,include
from views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^create$', create, name='create'),
    url(r'^destroy/(?P<course_id>\d+)$', destroy, name='destroy'),
    url(r'^confirmed/(?P<course_id>\d+)$', confirmed, name='confirmed'),
]