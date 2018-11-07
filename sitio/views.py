from django.utils import timezone
from .models import Perro, Adopcion, BlogPost, Slider
from django.contrib.auth.models import User
from .forms import PostForm, UserCreateForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
# Create your views here.
def home(request):
    page_title = "Mis Perris"
    posts = BlogPost.objects.order_by('published_date')
    slider = Slider.objects.order_by('published_date')
    args = {'page_title': page_title, 'posts':posts, 'slider':slider,}
    return render(request,'sitio/home.html', args)

# Usuario
def user_profile(request):
    perros = Perro.objects.filter(adoptador_por_id=request.user.id)
    args = {'user': request.user, 'perros': perros, }
    return render(request, 'user/user_profile.html', args )

def user_register(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            #inicia sesion en admin
            user = form.save()
            login(request, user)
            #cuando este creado lo mandamos a la lista de perros
            return redirect('perros')
    else:
        form = UserCreateForm()
    return render(request, 'user/form_reg.html', {'form':form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #inicia sesion en admin
            user = form.get_user()
            login(request, user)
            return redirect('perros')
    else:
        form = AuthenticationForm()
    return render(request, 'user/form_log.html', {'form':form})

def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('perros')

# Perros //grupos

def perros_todos(request):
    perros = Perro.objects.order_by('published_date')
    page_title = "Nuestros Perros"
    return render(request,'sitio/perros.html', {'perros' : perros , 'page_title': page_title})

def perros_adoptados(request):
    perros = Perro.objects.filter(estado='adoptado').order_by('published_date')
    page_title = "Perros Adoptados"
    return render(request,'sitio/perros.html', {'perros' : perros , 'page_title': page_title})

def perros_disponibles(request):
    perros = Perro.objects.filter(estado='disponibles').order_by('published_date')
    page_title = "Perros Disponibles para Adoptar"
    return render(request,'sitio/perros.html', {'perros' : perros , 'page_title': page_title})

def perros_rescatados(request):
    perros = Perro.objects.filter(estado='rescatado').order_by('published_date')
    page_title = "Perros Rescatados"
    return render(request,'sitio/perros.html', {'perros' : perros , 'page_title': page_title})

## Perros // individual

def perros_detail(request, pk):
    perro = get_object_or_404(Perro, pk=pk)
    return render(request, 'sitio/perros_detail.html', {'perro': perro})

def perros_new(request):
    if request.method == "POST":
        #form = PostForm(request.POST)
        form = PostForm(request.POST, request.FILES or None)
        if form.is_valid():
            Perro = form.save(commit=False)
            Perro.published_date = timezone.now()
            Perro.save()
            return redirect('perros_detail', pk=Perro.pk)
    else:
        form = PostForm()
        return render(request, 'sitio/perros_edit.html', {'form': form, 'page_name': 'Ingresar Perro'})

def perros_edit(request, pk):
    perro = get_object_or_404(Perro, pk=pk)
    if request.method == "POST":
        #form = PostForm(request.POST, instance=perro)
        form = PostForm(request.POST, request.FILES or None, instance=perro)
        if form.is_valid():
            perro = form.save(commit=False)
            perro.published_date = timezone.now()
            if perro.estado == 'adoptado':
                perro.adoptador_por_id = request.user.id
            else:
                perro.adoptador_por_id = None

            perro.save()
            return redirect('perros_detail', pk=perro.pk)
    else:
        form = PostForm(instance=perro)
    return render(request, 'sitio/perros_edit.html', {'form': form, 'name_page':'Editar Perro'})

def perros_delete(request, pk):
    perro = get_object_or_404(Perro, pk=pk)
    perro.delete()
    return redirect('perros')

def perros_update(request, pk):
    perro = get_object_or_404(Perro, pk=pk)
    perro.estado = "adoptado"
    perro.adoptador_por_id = request.user.id
    perro.published_date = timezone.now()
    perro.save()
    return redirect('user_profile')
