# django_app/views.py
from django.shortcuts import render, redirect
   
from .models import Photo
from .forms import PhotoForm

def upload(request):
  context = dict( backend_form = PhotoForm())

  if request.method == 'POST':
    form = PhotoForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('display')
  return render(request, 'upload.html', context)

def display(request):
    photos = Photo.objects.all()  # Retrieve all photos from the database
    return render(request, 'display.html', {'photos': photos})

