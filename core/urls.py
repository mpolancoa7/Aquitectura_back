from django.urls import path 
from .views import ProductosList

#Endpoints

urlpatterns = [
    path("api/productosall/",ProductosList.as_view())
]