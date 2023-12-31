# django_app/models.py
from django.db import models
from cloudinary.models import CloudinaryField

class Photo(models.Model):
    image = CloudinaryField('image')
    # Remove this when integrating Cloudinary
    # Django image field
    # image = models.ImageField(upload_to='photos/')
  