"""django_cloudinary_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

# django_app/urls.py
from django.urls import path
from django_app import views

# Remove these lines when integrating Cloudinary
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('upload/', views.upload, name='upload'),
    path('display', views.display, name='display')
]

# Remove this line when integrating Cloudinary
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


