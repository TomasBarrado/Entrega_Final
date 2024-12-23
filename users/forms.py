from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class UserEditForm(UserCreationForm):

    email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)
    

    class Meta:
        model = User
        fields = [
            'email',
            'password1',
            'password2',
        ]
        help_texts = {k:"" for k in fields}

from .models import Imagen

class ImagenForm(forms.ModelForm):
    """
    Formulario para gestionar las imágenes de perfil.
    """
    class Meta:
        model = Imagen
        fields = ['imagen']

        
