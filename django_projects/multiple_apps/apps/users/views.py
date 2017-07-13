# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

def register(request):
    return HttpResponse('placeholder for users to register a new user record')

def login(request):
    return HttpResponse('placeholder for users to login')


def users(request):
    return HttpResponse('placeholder to later display all the list of users')