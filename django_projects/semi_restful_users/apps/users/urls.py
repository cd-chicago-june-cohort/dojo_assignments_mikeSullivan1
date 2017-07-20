
from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^(?P<user_id>\d+)$', show, name='show'),
    url(r'^new$', new, name='new'),
    url(r'^edit/(?P<user_id>\d+)$', edit, name='edit'),
    url(r'^destroy/(?P<user_id>\d+)$', destroy, name='destroy'),
    url(r'^create$', create, name='create'),
    url(r'^update/(?P<user_id>\d+)$', update, name='update'),
]