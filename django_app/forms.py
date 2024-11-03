# django_app/forms.py
from django.forms import ModelForm     
from cloudinary.forms import CloudinaryFileField
from .models import Photo

class PhotoForm(ModelForm):
    image = CloudinaryFileField()

    class Meta:
        model = Photo
        fields = ['image']


        
        