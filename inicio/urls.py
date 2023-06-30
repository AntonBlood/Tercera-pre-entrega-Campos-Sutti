
from django.urls import path
from inicio import views

urlpatterns = [
    path('',views.inicio, name='inicio'),
    path('prueba/',views.prueba, name='prueba'),
    path('segunda-vista/',views.segunda_vista),
    path('bienvenida/<str:nombre>/<str:apellido>/',views.bienvenida),
    # path('crear-perro/<str:nombre>/<int:edad>/',views.crear_perro,name='crear_perro')
    path('perro/crear/',views.crear_perro,name='crear_perro'),
    path('persona/crear/',views.crear_persona,name='crear_persona'),
    path('compra/crear/',views.crear_compra,name='crear_compra'),

]
