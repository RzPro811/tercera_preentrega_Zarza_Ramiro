from django.urls import path
from merch.views import *

urlpatterns = [
    path("", inicio, name= "home"),
    path("productos/", productos, name="productos"),
    path("jeje/", cosoSecreto, name="secreto"),
    path("proximamente/", proximamente, name = "proximamente"),
    path("dvds/",DVD, name="DVDs"),
    path("distribuidor/", distribuidores, name="distribucion"),
#Formularios
    path("productosForm/",productosForm, name ="productosForm"),
    path("DVDForm/",DVDsForm, name ="dvdForm"),
    path("DistForm/", distForm, name = "distForm"),
#Busqueda
    path("buscar/", buscar, name= "srch"),
    path("encontrar/", encontrar, name= "find"),
]
