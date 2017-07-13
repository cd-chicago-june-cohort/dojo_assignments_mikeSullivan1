from django.conf.urls import url
from views import register,login,new_users, users

urlpatterns = [
    url(r'^register$', register),
    url(r'^login$', login),
    url(r'^users/new$', new_users),
    url(r'^users$', login),
]
