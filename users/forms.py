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

    # Obligatorios
    email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)
    # No obligatorios
    # last_name = forms.CharField()
    # first_name = forms.CharField()

    class Meta:
        model = User
        fields = [
            'email',
            'password1',
            'password2',
            # 'last_name',
            # 'first_name'
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

        