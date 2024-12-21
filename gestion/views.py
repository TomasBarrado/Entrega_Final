from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Mascota, Servicio, Veterinario
from .forms import MascotaForm
from django.views.generic import ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy


def inicio(request):
    return render(request, 'gestion/inicio.html')

def lista_veterinarios(request):
    veterinarios = Veterinario.objects.all()
    return render(request, 'gestion/lista_veterinarios.html', {'veterinarios': veterinarios})

def buscar_veterinario(request):
    query = request.GET.get('q', '')
    if query:
        veterinarios = Veterinario.objects.filter(nombre__icontains=query)
    else:
        veterinarios = Veterinario.objects.none()
    return render(request, 'gestion/buscar_veterinario.html', {'veterinarios': veterinarios, 'query': query})


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

# Vistas de lista de servicios y veterinarios sin LoginRequiredMixin
class ListaServiciosView(ListView):
    model = Servicio
    template_name = 'gestion/lista_servicios.html'
    context_object_name = 'servicios'

    def get_queryset(self):
        return Servicio.objects.all()  # Mostrar todos los servicios

class ListaVeterinariosView(ListView):
    model = Veterinario
    template_name = 'gestion/lista_veterinarios.html'
    context_object_name = 'veterinarios'


# Vistas de edición y eliminación con LoginRequiredMixin para protección
class EditarServicioView(LoginRequiredMixin, UpdateView):
    model = Servicio
    fields = ['nombre', 'descripcion']
    template_name = 'gestion/editar_servicio.html'
    context_object_name = 'servicio'

    def get_success_url(self):
        return reverse('lista_servicios')  # Redirige a la lista de servicios después de la edición

class EditarVeterinarioView(LoginRequiredMixin, UpdateView):
    model = Veterinario
    fields = ['nombre', 'matricula']
    template_name = 'gestion/editar_veterinario.html'
    context_object_name = 'veterinario'

    def get_success_url(self):
        return reverse('lista_veterinarios')

class EditarUsuarioView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'gestion/editar_usuario.html'
    fields = ['username', 'email', 'first_name', 'last_name']  # Campos a editar

    def get_success_url(self):
        return reverse('lista_usuarios')

# Rutas adicionales de usuario
class MascotasPorUsuarioView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Mascota
    template_name = 'gestion/mascotas_por_usuario.html'
    context_object_name = 'mascotas'

    def test_func(self):
        return self.request.user.is_staff  # Solo los administradores pueden ver las mascotas de los usuarios

    def get_queryset(self):
        return Mascota.objects.all()  # Muestra todas las mascotas


class ListaMascotasView(LoginRequiredMixin, ListView):
    model = Mascota
    template_name = 'gestion/lista_mascotas.html'
    context_object_name = 'mascotas'

    def get_queryset(self):
        return Mascota.objects.filter(dueño=self.request.user)  # Solo las mascotas del usuario logueado

class EditarMascotaView(LoginRequiredMixin, UpdateView):
    model = Mascota
    template_name = 'gestion/editar_mascota.html'
    fields = ['nombre', 'especie', 'raza', 'edad']  # Campos que deseas editar

    def get_queryset(self):
        return Mascota.objects.filter(dueño=self.request.user)  # Solo las mascotas del usuario logueado

class EliminarMascotaView(LoginRequiredMixin, DeleteView):
    model = Mascota
    template_name = 'gestion/eliminar_mascota.html'
    context_object_name = 'mascota'
    success_url = reverse_lazy('lista_mascotas')

    def get_queryset(self):
        return Mascota.objects.filter(dueño=self.request.user)  # Solo las mascotas del usuario logueado

class ListaUsuariosView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = User
    template_name = 'gestion/lista_usuarios.html'
    context_object_name = 'usuarios'

    def test_func(self):
        return self.request.user.is_staff