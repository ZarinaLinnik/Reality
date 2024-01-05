from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
# from .models import Users
# from .forms import name_class


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
            return redirect('you/')
    else:
        form = UserCreationForm()
    return render

@login_required
def creature(request): 
    return render(request, 'creature.html')

@login_required
def parameter1_who_are_you(request):
    return render(request, 'who_are_you.html')

def error404(request, exception=404):
    number = 404
    name = "Page Not Found"
    return render(request, 'error.html', {'error_number': number, 'error_name': name}, status=404)


# Help examples:
# posts = Post.objects.all()
# try-except-finally
# post = Post.objects.get(id=post_id)