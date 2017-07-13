from django.conf.urls import url
from views import index,display

urlpatterns = [
    url(r'^$', index),
    url(r'^display$', display),
]
