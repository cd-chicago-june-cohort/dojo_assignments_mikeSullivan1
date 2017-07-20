# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse
from django.template import RequestContext

from models import *

def index(request):
    all_courses = Course.objects.all()
    context= {
        "all_courses" : all_courses,
    }
    return render(request, "course_app/index.html",context)

def destroy(request, course_id):
    course = Course.objects.get(id = course_id)
    context= {
        "course" : course,
    }
    return render(request, "course_app/confirm.html", context)

def confirmed(request, course_id):
    course = Course.objects.get(id = course_id)
    course.delete()
    return redirect(reverse('index'))
    
def create(request):
    errors = {}
    if len(request.POST['name']) <= 10:
        errors["name"] = "Course name should be at least 10 characters"
    if len(request.POST['desc']) <= 15:
        errors["desc"] = "Course description should be at least 2 characters"

    if not len(errors):
        success = Course.objects.create(name = request.POST["name"], desc = request.POST["desc"])
        print success
    else:
        for key,value in errors:
            print "There is an error for %s: %S" % (key, value) 
    return redirect(reverse('index'))
    