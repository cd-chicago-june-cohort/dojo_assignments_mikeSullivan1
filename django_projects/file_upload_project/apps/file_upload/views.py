# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .forms import UploadFileForm

def index(request):
    return render(request, "file_upload/index.html")

def upload_file(request):
    if request.method == 'POST':
        print '1'
        form = UploadFileForm(request.POST, request.FILES)
        print '2'
#        if form.is_valid():           
        print '3'
        with open('mbs_new_file.txt', 'wb+') as destination:
            for chunk in request.FILES['file'].chunks():
                print '7'
                destination.write(chunk)
        print '8'
    #else:
    #    print '9'
    #    form = UploadFileForm()

    print '10'
    return redirect("/upload")

# Create your views here.
