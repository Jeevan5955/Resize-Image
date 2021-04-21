from django.contrib import messages
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from django.core.files.storage import FileSystemStorage


# Create your views here.


def index(request):
    form = ResizeForm()

    # if request.method == 'POST':
    #     form = ResizeForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         form = ResizeForm()

    return render(request, 'index.html', {'form': form})


def upload(request):

    if request.method == 'POST':
        form = ResizeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    details = Resize.objects.all().last()

    return render(request, 'image.html', {'details': details})
