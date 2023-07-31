from django import forms
from .models import Vehiculo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = "__all__"
        exclude = ['fecha_creacion','fecha_modoficacion']

class SignInForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username','email','password1','password2')
        permissions = ("visualizar_catalogo", "Es miembro con prioridad 1"),

    def save(self, commit=True):
        user = super(SignInForm,self).save(commit=False)
        user.email=self.cleaned_data['email']
        if commit:
            user.save()
        return user

