from rest_framework import serializers
from .models import Place

# con esto hemos definido nuestro modelo ahora vamos a crear nuestras migraciones a nuestra base de datos


class PlaceSerializer(serializers.ModelSerializer):

    class Meta:

        model = Place
        fields = '__all__'
