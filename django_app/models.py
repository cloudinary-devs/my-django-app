# django_app/models.py
from django.db import models
from cloudinary.models import CloudinaryField

class Photo(models.Model):
    image = CloudinaryField('image')
    # Remove Django image field when integrating Cloudinary
    # image = models.ImageField(upload_to='photos/')
  