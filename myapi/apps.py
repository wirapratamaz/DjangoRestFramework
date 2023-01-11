#digunakan untuk mengatur aplikasi Anda. File ini berisi sebuah kelas bernama 
#AppConfig, yang digunakan untuk mengatur berbagai pilihan dari aplikasi Anda
from django.apps import AppConfig


class MyapiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapi'
