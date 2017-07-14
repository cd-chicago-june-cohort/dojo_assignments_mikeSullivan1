from django.conf.urls import url, include
from views import *

urlpatterns = [
    url(r'^session_words$', index),
    url(r'^process$', process),
    url(r'^clear$', clear_session),
]
