# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

def index(request):
    return render(request,"cart/index.html")

def buy(request):
    print "Buy happened"
    request.session['transaction']=int(request.POST['quantity']) * float(request.POST['price']) 
    if 'total' not in request.session:
        request.session['total'] = request.session['transaction']
        request.session['items'] = int(request.POST['quantity'])
    else:
        request.session['total'] += request.session['transaction']
        request.session['items'] += int(request.POST['quantity'])
    request.session['curr_item']=request.POST['item']
    
    return redirect("/amadon/checkout")

def checkout(request):
    return render(request,"cart/checkout.html")

