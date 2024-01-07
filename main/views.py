from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.conf import settings
from django.shortcuts import render, redirect
from .models import Parameter1WhoAreYou, ParameterIMGMyPhoto
from .forms import AddParameter1WhoAreYou, AddParameterIMGMyPhoto
import datetime

media_url = settings.MEDIA_URL


def start(request):
    return render(request, 'start.html')

def registration(request): 
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/accounts/profile/')
    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {'form':form})

@login_required
def creature(request): 
    return render(request, 'creature.html')

@login_required
def add_parameter1_who_are_you(request):
    user = User.objects.get(username=request.user)
    if Parameter1WhoAreYou.objects.filter(user_id=user.id).exists() and request.method == 'GET':
        model = Parameter1WhoAreYou.objects.get(user_id=user.id)
        return render(request, 'show_content.html', {'model':model})
    
    if request.method == 'POST':
        form = AddParameter1WhoAreYou(request.POST)
        if form.is_valid():
            taken_info = form.save(commit=False)
            taken_info.date_time = datetime.datetime.now()
            taken_info.user = User.objects.get(username=request.user)
            taken_info.save()         
            return redirect('/who_are_you/')

    else:
        form = AddParameter1WhoAreYou()
    return render(request, 'who_are_you.html', {'form':form})

@login_required
def my_photo(request):
    user = User.objects.get(username=request.user)
    if ParameterIMGMyPhoto.objects.filter(user_id=user.id).exists() and request.method == 'GET':
        model = ParameterIMGMyPhoto.objects.get(user_id=user.id)
        return render(request, 'show_my_photo.html', {'image':model.image, 'media':media_url})
    
    if request.method == 'POST':
        form = AddParameterIMGMyPhoto(request.POST, request.FILES)
        if form.is_valid():
            taken_info = form.save(commit=False)
            taken_info.user = user
            taken_info.save()
            return redirect('/my_photo/')  
    else:
        form = AddParameterIMGMyPhoto()
    return render(request, 'my_photo.html', {'form': form})

@login_required
def log_out(request):
    logout(request)
    return redirect('/')

# def fill_in_parameter1(request):
#     return
# Надо в модели доп опредилитель, чтобы не обнулять

def error404(request, exception=404):
    number = 404
    name = "Page Not Found"
    return render(request, 'error.html', {'error_number': number, 'error_name': name}, status=404)

def error405(request, exception=405):
    number = 405
    name = "Method Not Allowed"
    return render(request, 'error.html', {'error_number': number, 'error_name': name}, status=405)


# Help examples:
# posts = Post.objects.all()
# try-except-finally
# post = Post.objects.get(id=post_id)