#Digunakan untuk mendefinisikan model database untuk aplikasi
from django.db import models


# Create your models here.
class Hero(models.Model):
    # fields on the model
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)
    
    # method return the string representation of the model
    def __str__(self):
        #this method returns the string representation of the primary key
        return self.name