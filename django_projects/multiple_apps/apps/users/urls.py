from django.conf.urls import url
from views import register, login, users

urlpatterns = [
    url(r'^register', register),
    url(r'^login', login),
    url(r'^users/new', register),
    url(r'^users', users),
]
