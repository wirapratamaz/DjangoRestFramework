#Digunakan untuk mengelola data pada aplikasi Anda melalui antarmuka web.
from django.contrib import admin
from .models import Hero

# Register your models here.
admin.site.register(Hero)