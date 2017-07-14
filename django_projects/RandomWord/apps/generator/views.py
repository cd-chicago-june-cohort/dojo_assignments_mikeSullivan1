# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.crypto import get_random_string 

from django.shortcuts import render

def index(request):
    if "counter" not in request.session:
        request.session['counter'] = 0
    request.session['counter'] += 1
    context =   {
                "random": get_random_string(length=14),
                "counter": request.session['counter']
                }
    return render(request,'generator/index.html',context)


# Create your views here.
