# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse
from django.template import RequestContext

from models import *



# errors = Blog.objects.basic_validator(request.POST)


def index(request):
    all_users = User.objects.all()
    context= {
        "all_users" : all_users,
    }
    return render(request, "users/index.html",context)

def show(request,user_id):
    users = User.objects.get(id = user_id)
    context= {
        "users" : users,
    }
    
    return render(request, "users/show.html", context)

def new(request):
    return render(request, "users/new.html")

def edit(request, user_id):
    users = User.objects.get(id = user_id)
    context= {
        "users" : users,
    }
    return render(request, "users/edit.html", context)

def destroy(request, user_id):
    user = User.objects.get(id = user_id)
    user.delete()
    return redirect(reverse('users:index'))

def create(request):
    errors = {}
    if len(request.POST['first_name']) <= 2 or len(request.POST['email']) > 30:
        errors["first_name"] = "Blog name should be at least 2 characters"
    if len(request.POST['last_name']) <= 2 or len(request.POST['email']) > 30 :
        errors["last_name"] = "Blog name should be at least 2 characters"
    if len(request.POST['email']) <5 or len(request.POST['email']) >40:
        errors["email"] = "Blog desc should be more than 10 characters"  

    if not len(errors):
        success = User.objects.create(first_name = request.POST["first_name"], last_name = request.POST["last_name"],email = request.POST["email"])
        print success
    else:
        for key,value in errors:
            print "There is an error for %s: %S" % (key, value) 
    return redirect(reverse('users:index'))

def update(request,user_id):

    request.session.errors = []
    if len(request.POST['first_name']) <= 2 or len(request.POST['email']) > 30:
        request.session.errors.append("There is an error: First Name should be at least 2 characters and less than 30 characters")
    if len(request.POST['last_name']) <= 2 or len(request.POST['email']) > 30 :
        request.session.errors.append("There is an error: Last Name should be at least 2 characters and less than 30 characters")
    if len(request.POST['email']) <5 or len(request.POST['email']) >40:
        request.errors["email"] = "There is an error: Email should be at least 5 characters and less than 40 characters"  

    if not len(request.session.errors):
        update_user = User.objects.get(id = user_id)
        update_user.first_name = request.POST['first_name']
        update_user.last_name = request.POST['last_name']
        update_user.email = request.POST['email']
        update_user.save()
        print "success"
        return redirect(reverse('users:index'))
    else:
        return redirect(reverse('users:edit', kwargs={"user_id" : user_id}))


# Create your views here.
