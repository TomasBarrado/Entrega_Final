from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Mascota, Servicio, Veterinario
from .forms import MascotaForm

def inicio(request):
    return render(request, 'gestion/inicio.html')

@login_required
def lista_mascotas(request):
    mascotas = Mascota.objects.filter(dueño=request.user)
    return render(request, 'gestion/lista_mascotas.html', {'mascotas': mascotas})

@login_required
def agregar_mascota(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            mascota = form.save(commit=False)
            mascota.dueño = request.user
            mascota.save()
            return redirect('lista_mascotas')
    else:
        form = MascotaForm()
    return render(request, 'gestion/agregar_mascota.html', {'form': form})

@login_required
def editar_mascota(request, pk):
    mascota = get_object_or_404(Mascota, pk=pk, dueño=request.user)
    if request.method == 'POST':
        form = MascotaForm(request.POST, instance=mascota)
        if form.is_valid():
            form.save()
            return redirect('lista_mascotas')
    else:
        form = MascotaForm(instance=mascota)
    return render(request, 'gestion/editar_mascota.html', {'form': form})

@login_required
def eliminar_mascota(request, pk):
    mascota = get_object_or_404(Mascota, pk=pk, dueño=request.user)
    if request.method == 'POST':
        mascota.delete()
        return redirect('lista_mascotas')
    return render(request, 'gestion/eliminar_mascota.html', {'mascota': mascota})

def lista_servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'gestion/lista_servicios.html', {'servicios': servicios})

def lista_veterinarios(request):
    veterinarios = Veterinario.objects.all()
    return render(request, 'gestion/lista_veterinarios.html', {'veterinarios': veterinarios})

def buscar_veterinario(request):
    query = request.GET.get('q', '')
    if query:
        veterinarios = Veterinario.objects.filter(nombre__icontains=query)
    else:
        veterinarios = []
    return render(request, 'gestion/buscar_veterinario.html', {'veterinarios': veterinarios, 'query': query})