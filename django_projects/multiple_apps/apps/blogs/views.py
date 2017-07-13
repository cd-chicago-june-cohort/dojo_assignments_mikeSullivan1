# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(response):
    return HttpResponse('Blog Home')

def new(response):
    return HttpResponse('New Blog Display')

def create(response):
    return redirect('/blogs')

def show(response, number):
    return HttpResponse("placeholder to display blog #" + number)

def edit(response, number):
    return HttpResponse("placeholder to edit blog #" + number)

def destroy(response,number):
    return redirect('/blogs')

