# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

from django.shortcuts import render

def index(request):
    context = {
    "date": strftime("%Y-%M-%d", gmtime()),
    "time": strftime("%H:%M %p", gmtime()),
    "check": "this is to see if the var works"
    }
    return render(request,'time_display_app/index.html', context)

# Create your views here.
