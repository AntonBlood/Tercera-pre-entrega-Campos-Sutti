from django.http import HttpResponse
from django.template import Template, Context, loader
from inicio.models import Perro,Persona,Compra
from django.shortcuts import render

#v1
# def inicio(request):
#     return HttpResponse('Hola mundo')

#v2
# def inicio(request):
#     archivo=open(r'C:\Users\lenovo\Desktop\preentrega3\templates\inicio.html','r')
    
#     template=Template(archivo.read())
    
#     archivo.close()
    
#     diccionario={
#         'mensaje': 'Este es el mensaje',
        
#     }
    
#     contexto=Context(diccionario)
    
#     renderizar_template=template.render(contexto)
    
#     return HttpResponse(renderizar_template)

#v3   con cargadores

# def inicio(request):
        
#     template=loader.get_template('inicio.html')
    
#     diccionario={
#         'mensaje': 'Este es el mensaje',
        
#     }
#     renderizar_template=template.render(diccionario)
    
#     return HttpResponse(renderizar_template)

#v4

def prueba(request):
        
    diccionario={
        'mensaje': 'Este es el mensaje',
    }
    return render(request,'inicio/prueba.html',diccionario)


def inicio(request):
    return render(request,'inicio/inicio.html')


def segunda_vista(request):
    return HttpResponse('<h1>segunda vista</h1>')

def saludar(request):
    return HttpResponse('Bienvenido')

def bienvenida(request, nombre, apellido):
    return HttpResponse(f'Bienvenido {nombre.title()} {apellido.title()}')


def crear_perro(request):
    
    
    
    print('-----------------------------------------------')
    print(request.POST)
    print('-----------------------------------------------')
    print(request.GET)
    
    diccionario={}
    
    if request.method == 'POST':
        perro=Perro(nombre=request.POST['nombre'],edad=request.POST['edad'])
        perro.save()
        diccionario['perro']=perro
    return render(request,'inicio/crear_perro.html',diccionario)


def crear_persona(request):
    
    print('-----------------------------------------------')
    print(request.POST)
    print('-----------------------------------------------')
    print(request.GET)
    
    diccionario={}
    
    if request.method == 'POST':
        persona=Persona(nombre=request.POST['nombre'],apellido=request.POST['apellido'],dni=request.POST['dni'])
        persona.save()
        diccionario['persona']=persona
    return render(request,'inicio/crear_persona.html',diccionario)



def crear_compra(request):

    print('-----------------------------------------------')
    print(request.POST)
    print('-----------------------------------------------')
    print(request.GET)
    
    diccionario={}
    
    if request.method == 'POST':
        compra=Compra(cantidad=request.POST['cantidad'],producto=request.POST['producto'])
        compra.save()
        diccionario['compra']=compra
    return render(request,'inicio/crear_compra.html',diccionario)