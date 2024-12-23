from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm, UserEditForm, ImagenForm
from django.contrib import messages
from .models import Imagen



def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('inicio')  
    else:
        form = RegistroForm()
    return render(request, 'users/registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('inicio')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

@login_required
def perfil(request):
    return render(request, 'users/perfil.html')

  
@login_required
def editar_perfil(request):
    usuario = request.user  

    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST, request.FILES, instance=usuario) 

        if miFormulario.is_valid():
            if miFormulario.cleaned_data.get('imagen'):
                if Imagen.objects.filter(user=usuario).exists():
                    usuario.imagen.imagen = miFormulario.cleaned_data.get('imagen')
                    usuario.imagen.save()
                else:
                    avatar = Imagen(user=usuario, imagen=miFormulario.cleaned_data.get('imagen'))
                    avatar.save()

            miFormulario.save()

            messages.success(request, '¡Tu contraseña ha sido cambiada exitosamente!')
            return redirect('perfil') 
    else:
        miFormulario = UserEditForm(instance=usuario) 

    return render(request, "users/editar_usuario.html", {"mi_form": miFormulario, "usuario": usuario})


@login_required
def agregar_imagen(request):
    """
    Vista para agregar o actualizar la imagen de perfil del usuario.
    """
    user = request.user  

    try:
        imagen = user.avatar
    except Imagen.DoesNotExist:
        imagen = None

    if request.method == "POST":
        form = ImagenForm(request.POST, request.FILES, instance=imagen)
        if form.is_valid():
            nueva_imagen = form.save(commit=False)
            nueva_imagen.user = user
            nueva_imagen.save()
            return redirect("perfil") 
    else:
        form = ImagenForm(instance=imagen)

    return render(request, "users/agregar_imagen.html", {"form": form})


