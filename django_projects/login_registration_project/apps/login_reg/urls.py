from django.conf.urls import url

from views import *


urlpatterns = [
    url(r'^$', index, name="home"),
    url(r'^authenticate$', authenticate, name="authenticate"),
    url(r'^success$', success, name="success"),
    url(r'^logout$', logout, name="logout"),
]

