from rest_framework import generics 
from .serializers import ProductosSerializer 
from .models import Productos

#desactivar momentaneamente el token
from rest_framework.permissions import AllowAny

class ProductosList(generics.ListAPIView):
    #select * from productos
    queryset = Productos.objects.all()
    serializer_class=ProductosSerializer
    #desactivar momentaneamente el token
    permission_classes = (AllowAny,)

