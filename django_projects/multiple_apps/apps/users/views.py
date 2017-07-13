# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

def register():
    return HttpResponse('placeholder for users to register a new user record')

def login():
    return HttpResponse('placeholder for users to login')

def new_users():
    return HttpResponse('placeholder for users to create a new user record')

def users():
    return HttpResponse('placeholder to later display all the list of users')
# Create your views here.
