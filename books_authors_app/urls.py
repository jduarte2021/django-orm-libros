from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('ingresar_libro', views.ingresar_libro),
    path('autores', views.autor),
    path('ingresar_autor', views.ingresar_autor),
    path('libro_info/<int:id>', views.libro_info),
    path('autor_info/<int:id>', views.autores_info),

]
