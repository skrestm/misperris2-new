from django import forms
from .models import Perro
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PostForm(forms.ModelForm):

    class Meta:
        model = Perro
        fields = ('fotografia','nombre', 'raza','descripcion', 'estado',)

class UserCreateForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ("username", "first_name","last_name","email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        if commit:
            user.save()
        return user       
     