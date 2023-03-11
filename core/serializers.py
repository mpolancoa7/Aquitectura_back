from rest_framework import serializers 
from .models import Productos

class ProductosSerializer(serializers.ModelSerializer): 
    class Meta: 
        model= Productos 
        fields = '__all__'
        #fields = ('id', 'nombre') por si quieres solo algunos

