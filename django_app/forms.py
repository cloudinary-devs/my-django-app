# django_app/forms.py
from django.forms import ModelForm     
from cloudinary.forms import CloudinaryFileField
from .models import Photo

class PhotoForm(ModelForm):
    image = CloudinaryFileField()

    class Meta:
        model = Photo
        fields = '__all__'

    def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.fields['image'].options={
           'tags': 'new_image',
           'format': 'png'

    }
        
        