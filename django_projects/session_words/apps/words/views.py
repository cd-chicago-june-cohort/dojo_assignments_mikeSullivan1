# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import time

from django.shortcuts import render, redirect

def index(request): 
    if 'log' not in request.session:
        request.session['log']=[]  
    context = {
                "log" : request.session['log']
    }
    return render(request, "words/index.html", context)

def process(request):
    if 'word' not in request.POST:
        return redirect('/session_words')
    else:
        word = request.POST['word']

    if 'color' in request.POST:
        color = request.POST['color']
    else:
        color = 'black'
            
    if 'font' in request.POST:
        large_font = 6
    else:
        large_font = 4
    curr_trans = {
            "word" : word,
            "color": color,
            "large_font" : large_font,
            "timestamp" : time.strftime('%a %H:%M:%S'),
    }
    temp = request.session['log']
    temp.insert(0,curr_trans)
    request.session['log'] = temp

    return redirect('/session_words')

def clear_session(request):
    request.session.clear()
    return redirect('/session_words')

