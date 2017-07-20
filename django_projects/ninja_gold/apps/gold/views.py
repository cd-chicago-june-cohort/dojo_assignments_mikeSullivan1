# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random
from datetime import datetime

from django.shortcuts import render, redirect

def index(request):
    return render(request, "gold/index.html")

def process(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
        request.session['log'] = []

    currloc = request.POST['building']
    if currloc =='farm':
        gold = random.randint(10,20)
    elif currloc == 'cave':
        gold = random.randint(5,10)
    elif currloc == 'house':
        gold = random.randint(2,5)
    elif currloc == 'casino':
        gold = random.randint(-50,50) 
          
    curr_trans = {
                "location" : currloc,
                "amount" : gold,
                "timestamp":'{:%Y-%b-%d %H:%M:%S}'.format(datetime.now()),
                }
    temp = request.session['log']
    temp.insert(0,curr_trans)
    request.session['log'] = temp
    y = request.session['gold'] 
    y += gold
    request.session['gold'] = y
    print request.session['gold']
    print request.session['log']
    return redirect('/')

# Create your views here.
