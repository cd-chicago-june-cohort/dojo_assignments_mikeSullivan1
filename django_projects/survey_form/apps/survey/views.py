# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

def index(request):
    return render(request, 'survey/index.html')

def result(request):
    return render(request, 'survey/result.html')

def process(request):
    if "counter" not in request.session:
        request.session['counter'] = 0
    request.session['counter'] +=1
    request.session['user_name'] = request.POST['user_name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    return redirect('/result')

# Create your views here.
