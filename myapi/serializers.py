#Serialization is the process of converting a Model to JSON
#The serializer will turn our heroes into a JSON representation so the API
from rest_framework import serializers
from .models import Hero

# convert the "Hero" model into a format that can be easily rendered into JSON
class HeroSerializer(serializers.HyperlinkedModelSerializer):
    #The Meta class contains metadata about the serializer
    class Meta:
        #model attribute as 'Hero
        model = Hero
        # fields attribute
        fields = ('name', 'alias')