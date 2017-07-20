# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, reverse, redirect
from django.contrib import messages
from models import *


# Create your views here.
def index(request):
    # if 'current_first_name' not in request.session:
    #     request.session['current_first_name'] = ''
    # if 'current_last_name' not in request.session:
    #     request.session['current_last_name'] = ''
    # if 'current_email' not in request.session:
    #     request.session['current_email'] = ''
    if request.session['current_email'] != '':
        redirect ("/success")
    return render(request, 'login_reg/index.html')

def authenticate(request):
    if request.method !='POST':
        return redirect('/')

    new_user=False

    #error handling
    if request.POST['auth_type']=='register':
        new_user = True
        errors=User.objects.register_validator(request.POST)
    else:
        errors=User.objects.login_validator(request.POST)

    if len(errors):
        for error,error_message in errors.iteritems():
            messages.error(error_message)
        return redirect('/')

    email = request.POST['email']
    password = request.POST['password']
    if new_user:
        first_name = request.POST['first_name']
        print first_name
        last_name = request.POST['last_name']
        print last_name
        birthday = request.POST['birthday']
        print birthday
        confirm = request.POST['confirm']
        print confirm
        hashed_key=bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        print hashed_key
        User.objects.create(first_name = first_name, last_name = last_name, email = email, password=hashed_key,birthday=birthday)
        request.session['current_first_name'] = first_name
        request.session['current_last_name'] = last_name            
    else:
        this_user=User.objects.get(email=email)
        request.session['current_first_name'] = this_user.first_name
        print request.session['current_first_name']
        request.session['current_last_name'] = this_user.last_name
        print request.session['current_last_name']
    request.session['current_email'] = email
        
    return redirect("/success")

def success(request):
    # return render_template('success.html')
    context= {
        "email" : request.session['current_email'],
        "first" : request.session['current_first_name'],
        "last" : request.session['current_last_name'],
    }
    return render(request, "login_reg/success.html", context)

def logout(request):
    request.session['current_first_name'] = ''
    request.session['current_last_name'] = ''
    request.session['current_email'] = ''
    return redirect('/')