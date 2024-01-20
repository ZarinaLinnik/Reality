from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from .models import ParameterIMGMyPhoto, Parameter1WhoAreYou, Parameter2WhatDoYouDo, Parameter3Environment, Parameter4Habits, Parameter5FreeTime, Parameter6Appearance, Parameter7Behavior, Parameter8Mind
from .forms import GiveFeedBack, AddParameterIMGMyPhoto, AddParameter1WhoAreYou, AddParameter2WhatDoYouDo, AddParameter3Environment, AddParameter4Habits, AddParameter5FreeTime, AddParameter6Appearance, AddParameter7Behavior, AddParameter8Mind
import datetime
import logging


media_url = settings.MEDIA_URL
logger = logging.getLogger('main')


def start(request, farewell=False):
    return render(request, 'start.html', {'goodbye_words':farewell})


def registration(request): 
    special_text = False
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
            special_text = True
    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {'form':form, 'special_text':special_text})


@login_required
def feedback(request):
    form = GiveFeedBack()
    if request.method == 'POST':
        username = request.user
        email = request.POST['email']
        subject = request.POST['subject']
        message = f'\tFrom {email}\n\n\t' + request.POST['message'] + f'\n\n\tBy {username}'

        send_mail(subject, message, email, ['test123testZarina@gmail.com',])

        text = 'Thank you for your answer!'
    else:
        text = ''
    return render(request, 'feedback.html', {'feedback_fields': form, 'thank_you_text':text})


@login_required
def creature(request): 
    logger.log(20, "\"I'm on the main page. 'Creature'! Me and you\"")
    return render(request, 'creature.html')


@login_required
def log_out(request):
    logout(request)
    return start(request, True)


@login_required
def my_photo(request):
    user = User.objects.get(username=request.user)
    if ParameterIMGMyPhoto.objects.filter(user_id=user.id).exists() and request.method == 'GET':
        model = ParameterIMGMyPhoto.objects.get(user_id=user.id)
        return render(request, 'show_my_photo.html', {'model':model, 'media':media_url})
    
    if request.method == 'POST':
        form = AddParameterIMGMyPhoto(request.POST, request.FILES)
        if form.is_valid():
            taken_info = form.save(commit=False)
            taken_info.user = user
            taken_info.date_time = datetime.datetime.now()
            taken_info.save()
            return redirect('/my_photo/')  
    else:
        form = AddParameterIMGMyPhoto()
    return render(request, 'my_photo.html', {'form': form})


@login_required
def add_parameter1_who_are_you(request):
    user = User.objects.get(username=request.user)
    if Parameter1WhoAreYou.objects.filter(user_id=user.id).exists() and request.method == 'GET':
        model = Parameter1WhoAreYou.objects.get(user_id=user.id)
        return render(request, 'show_who_are_you.html', {'model':model})
    
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


def add_parameter2_what_do_you_do(request): 
    user = User.objects.get(username=request.user)
    if Parameter2WhatDoYouDo.objects.filter(user_id=user.id).exists() and request.method == 'GET':
        model = Parameter2WhatDoYouDo.objects.get(user_id=user.id)
        return render(request, 'show.html', {'model':model})
    
    if request.method == 'POST':
        form = AddParameter2WhatDoYouDo(request.POST)
        if form.is_valid():
            taken_info = form.save(commit=False)
            taken_info.date_time = datetime.datetime.now()
            taken_info.user = User.objects.get(username=request.user)
            taken_info.save()         
            return redirect('/what_do_you_do/')
    else:
        form = AddParameter2WhatDoYouDo()
    return render(request, 'what_do_you_do.html', {'form':form})


def add_parameter3_environment(request): 
    user = User.objects.get(username=request.user)
    if Parameter3Environment.objects.filter(user_id=user.id).exists() and request.method == 'GET':
        model = Parameter3Environment.objects.get(user_id=user.id)
        return render(request, 'show.html', {'model':model})
    
    if request.method == 'POST':
        form = AddParameter3Environment(request.POST)
        if form.is_valid():
            taken_info = form.save(commit=False)
            taken_info.date_time = datetime.datetime.now()
            taken_info.user = User.objects.get(username=request.user)
            taken_info.save()         
            return redirect('/environment/')
    else:
        form = AddParameter3Environment()
    return render(request, 'questions.html', {'form':form, 'main_question':'What does your room or environment look like?'})


def add_parameter4_habits(request): 
    user = User.objects.get(username=request.user)
    if Parameter4Habits.objects.filter(user_id=user.id).exists() and request.method == 'GET':
        model = Parameter4Habits.objects.get(user_id=user.id)
        return render(request, 'show.html', {'model':model})
    
    if request.method == 'POST':
        form = AddParameter4Habits(request.POST)
        if form.is_valid():
            taken_info = form.save(commit=False)
            taken_info.date_time = datetime.datetime.now()
            taken_info.user = User.objects.get(username=request.user)
            taken_info.save()         
            return redirect('/habits/')
    else:
        form = AddParameter4Habits()
    return render(request, 'questions.html', {'form':form, 'main_question':'What are your habits?'})


def add_parameter5_free_time(request): 
    user = User.objects.get(username=request.user)
    if Parameter5FreeTime.objects.filter(user_id=user.id).exists() and request.method == 'GET':
        model = Parameter5FreeTime.objects.get(user_id=user.id)
        return render(request, 'show.html', {'model':model})
    
    if request.method == 'POST':
        form = AddParameter5FreeTime(request.POST)
        if form.is_valid():
            taken_info = form.save(commit=False)
            taken_info.date_time = datetime.datetime.now()
            taken_info.user = User.objects.get(username=request.user)
            taken_info.save()         
            return redirect('/free_time/')
    else:
        form = AddParameter5FreeTime()
    return render(request, 'questions.html', {'form':form, 'main_question':'How do you spend your free time?'})


def add_parameter6_appearance(request): 
    user = User.objects.get(username=request.user)
    if Parameter6Appearance.objects.filter(user_id=user.id).exists() and request.method == 'GET':
        model = Parameter6Appearance.objects.get(user_id=user.id)
        return render(request, 'show.html', {'model':model})
    
    if request.method == 'POST':
        form = AddParameter6Appearance(request.POST)
        if form.is_valid():
            taken_info = form.save(commit=False)
            taken_info.date_time = datetime.datetime.now()
            taken_info.user = User.objects.get(username=request.user)
            taken_info.save()         
            return redirect('/appearance/')
    else:
        form = AddParameter6Appearance()
    return render(request, 'questions.html', {'form':form, 'main_question':'What do you look like?'})

    
def add_parameter7_behavior(request): 
    user = User.objects.get(username=request.user)
    if Parameter7Behavior.objects.filter(user_id=user.id).exists() and request.method == 'GET':
        model = Parameter7Behavior.objects.get(user_id=user.id)
        return render(request, 'show.html', {'model':model})
    
    if request.method == 'POST':
        form = AddParameter7Behavior(request.POST)
        if form.is_valid():
            taken_info = form.save(commit=False)
            taken_info.date_time = datetime.datetime.now()
            taken_info.user = User.objects.get(username=request.user)
            taken_info.save()         
            return redirect('/behavior/')
    else:
        form = AddParameter7Behavior()
    return render(request, 'questions.html', {'form':form, 'main_question':'What is your behavior like?'})


def add_parameter8_mind(request): 
    user = User.objects.get(username=request.user)
    if Parameter8Mind.objects.filter(user_id=user.id).exists() and request.method == 'GET':
        model = Parameter8Mind.objects.get(user_id=user.id)
        return render(request, 'show.html', {'model':model})
    
    if request.method == 'POST':
        form = AddParameter8Mind(request.POST)
        if form.is_valid():
            taken_info = form.save(commit=False)
            taken_info.date_time = datetime.datetime.now()
            taken_info.user = User.objects.get(username=request.user)
            taken_info.save()         
            return redirect('/mind/')
    else:
        form = AddParameter8Mind()
    return render(request, 'questions.html', {'form':form, 'main_question':'How do you think?'})


def error400(request, exception=400):
    name = "Bad Request"
    return render(request, 'error.html', {'error_number': exception.numerator, 'error_name': name}, status=exception.numerator)

def error403(request, exception=403):
    name = "Forbidden"
    return render(request, 'error.html', {'error_number': exception.numerator, 'error_name': name}, status=exception.numerator)

def error404(request, exception=404):
    name = "Page Not Found"
    return render(request, 'error.html', {'error_number': exception.numerator, 'error_name': name}, status=exception.numerator)

def error405(request, exception=405):
    name = "Method Not Allowed"
    return render(request, 'error.html', {'error_number': exception.numerator, 'error_name': name}, status=exception.numerator)

def error500(request, exception=500):
    name = "Internal Server Error"
    return render(request, 'error.html', {'error_number': exception.numerator, 'error_name': name}, status=exception.numerator)