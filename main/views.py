from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Users
# from .forms import name_class


def authorization(request): pass

def registration(request): pass

def creature(request): 
    return render(request, 'creature.html')

# def each_parameter(request, parameter):
#     return HttpResponse('<h1>it works "' + parameter + '" </h1>')

def error404(request, exception=404):
    number = 404
    name = "Page Not Found"
    return render(request, 'error.html', {'error_number': number, 'error_name': name}, status=404)


# Help examples:
# posts = Post.objects.all()
# try-except-finally
# post = Post.objects.get(id=post_id)