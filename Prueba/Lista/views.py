from django.shortcuts import render, redirect
from .models import producto
from .forms import formulario_producto
def agregar_producto(request):
    producto_agregar=formulario_producto(request.POST)
    if producto_agregar.is_valid():
        producto_agregar.save()
    return redirect('lista_producto')
def lista_producto(request):
    listado = producto.objects.all()
    mostrar_formulario = formulario_producto()
    return render(request, 'Lista.html', {'listado':listado, 'mostrar_formulario':mostrar_formulario})
def eliminar_producto(request, id_producto):
    producto_buscado=producto.objects.get(id=id_producto)
    producto_buscado.delete()
    return redirect('lista_producto')
def editar_producto(request, id_producto):
    producto_buscado=producto.objects.get(id=id_producto)
    if request.method == 'GET':
        formulario_editar=formulario_producto(instance=producto_buscado)
        return render(request, 'Editar.html', {'formulario_editar':formulario_editar, 'id_producto':id_producto})
    if request.method == 'POST':
        formulario_editar=formulario_producto(request.POST, instance=producto_buscado)
        if formulario_editar.is_valid():
            formulario_editar.save()
            return redirect('lista_producto')      
    return render(request, 'Editar.html', {'formulario_editar': formulario_producto(instance=producto_buscado), 'id_producto': id_producto})