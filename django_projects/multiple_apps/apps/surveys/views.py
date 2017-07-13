# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

def index(response):
    return HttpResponse("placeholder to display all the surveys created")


def display(response):
    return HttpResponse("placeholder for users to add a new survey")

