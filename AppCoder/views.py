from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import *
from AppCoder.forms import *

# Create your views here.

def inicio(request):
    return render(request,'AppCoder/busqueda_productos.html')
   #return render(request,'AppCoder/inicio.html')

def busqueda_productos(request):
    return render(request, "AppCoder/busqueda_productos.html")

def buscar(request):
    
    if request.GET['prd']:
        #mensaje="articulo buscado: %r" %request.GET['prd']
        producto=request.GET['prd']
        
        articulos=Pais.objects.filter(pais_origen__icontains=producto)
        
        return render(request,"AppCoder/resultados_busqueda.html", {"articulos":articulos, "query": producto})
        
        
    else:
        mensaje="No ingresaste texto"
    
    return HttpResponse(mensaje)

def productos(request):
    if request.method == 'POST':
        miFormulario = ProductosFormulario(request.POST)
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            productos = Productos(nombre=informacion['nombre'])
            productos.save()
            return render(request,'AppCoder/busqueda_productos.html/')
    else:
        miFormulario = ProductosFormulario()
        
    return render(request,'AppCoder/formularioInsert_producto.html', {"miFormulario":miFormulario})
    
    #return render(request,'AppCoder/profesores.html')


def consultas(request):
    if request.method == 'POST':
        miFormulario = ConsultasFormulario(request.POST)
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            consultas = Consultas(nombre=informacion['nombre'], 
                                  apellido=informacion['apellido'],
                                   email=informacion['email'],
                                    consulta=informacion['consulta'])
            consultas.save()
            return render(request,'AppCoder/busqueda_productos.html/')
    else:
        miFormulario = ConsultasFormulario()
        
    return render(request,'AppCoder/formularioInsert_consulta.html', {"miFormulario":miFormulario})
    
    #return render(request,'AppCoder/estudiantes.html')
  

def sucursales(request):
    if request.method == 'POST':
        miFormulario = SucursalesFormulario(request.POST)
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            sucursales = Sucursales(ubicacion=informacion['ubicacion'],
                                    numero=informacion['numero'],
                                    nombre_encargado=informacion['nombre_encargado'])
            sucursales.save()
            return render(request,'AppCoder/busqueda_productos.html')
    else:
        miFormulario = SucursalesFormulario()
        
    return render(request,'AppCoder/formularioInsert_sucursal.html', {"miFormulario":miFormulario})