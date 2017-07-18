from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^upload$', index),
    url(r'^upload/file', upload_file),
]