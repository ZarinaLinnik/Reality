from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from .models import ParameterIMGMyPhoto as MyPhoto, Parameter1WhoAreYou as WhoAreYou, Parameter2WhatDoYouDo , Parameter3Environment, Parameter4Habits, Parameter5FreeTime, Parameter6Appearance, Parameter7Behavior, Parameter8Mind
from .forms import GiveFeedBack, AddParameterIMGMyPhoto as AddMyPhoto, AddParameter1WhoAreYou as AddWhoAreYou, AddParameter2WhatDoYouDo, AddParameter3Environment, AddParameter4Habits, AddParameter5FreeTime, AddParameter6Appearance, AddParameter7Behavior, AddParameter8Mind
import datetime
import logging
import os


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
    user = User.objects.get(username=request.user)
    try:
        image_way = MyPhoto.objects.get(user_id=user.id).image
    except ObjectDoesNotExist:
        image_way = None
    return render(request, 'creature.html', {'media': media_url, 'image':image_way})


@login_required
def log_out(request):
    logout(request)
    return start(request, True)


@login_required
def delete_account(request):
    User.objects.filter(username=request.user).delete()
    return redirect('start')


def save_taken_info(form, user):
    taken_info = form.save(commit=False)
    taken_info.user = user
    taken_info.date_time = datetime.datetime.now()
    taken_info.save()


@login_required
def my_photo(request):
    user = User.objects.get(username=request.user)
    if request.method == 'POST':
        form = AddMyPhoto(request.POST, request.FILES)
        if MyPhoto.objects.filter(user_id=user.id).exists():
            if form.is_valid():
                past_image = str(MyPhoto.objects.get(user_id=user.id).image)
                try:
                    os.remove(os.path.join('media', past_image))
                except FileNotFoundError:
                    logger.debug(f"Not found this img way: {os.path.join('media', past_image)}")
                MyPhoto.objects.filter(user_id=user.id).delete()
                save_taken_info(form, user)
            else:
                return render(request, 'my_photo.html', {'form': form})
        else:
            if form.is_valid():
                save_taken_info(form, user)
            else:
                return render(request, 'my_photo.html', {'form': form})
        return redirect('/my_photo/')    
                    
    else:
        form = AddMyPhoto()
        if MyPhoto.objects.filter(user_id=user.id).exists():
            model = MyPhoto.objects.get(user_id=user.id)
            return render(request, 'show_my_photo.html', {'model':model, 'media':media_url, 'form':form})
        else:
            return render(request, 'my_photo.html', {'form': form})


@login_required
def add_parameter1_who_are_you(request):
    user = User.objects.get(username=request.user)
    if request.method == 'POST':
        form = AddWhoAreYou(request.POST)
        if WhoAreYou.objects.filter(user_id=user.id).exists():
            if form.is_valid():
                form_text0 = form.cleaned_data['text0']
                form_changes = form.cleaned_data['changes']
                form_wwh = form.cleaned_data['what_why_how']
                form_name = form.cleaned_data['name']
                form_surname = form.cleaned_data['surname']
                form_goals = form.cleaned_data['goals']
                WhoAreYou.objects.filter(user_id=user.id).update(
                    text0=form_text0, 
                    changes=form_changes, 
                    what_why_how=form_wwh, 
                    date_time=datetime.datetime.now(), 
                    name=form_name, 
                    surname=form_surname, 
                    goals=form_goals
                    )
        else:
            if form.is_valid():
                save_taken_info(form, user)         
        return redirect('/who_are_you/')                   
    else:
        if WhoAreYou.objects.filter(user_id=user.id).exists():
            model = WhoAreYou.objects.get(user_id=user.id)
            form = AddWhoAreYou(instance=model)
            date_time = model.date_time
            return render(request, 'show_who_are_you.html', {'date_time':date_time, 'form':form})
        else:
            form = AddWhoAreYou()
            return render(request, 'who_are_you.html', {'form':form}) 
    

def update_model(form, user, class_model):
    form_text0 = form.cleaned_data['text0']
    form_text1 = form.cleaned_data['text1']
    form_text2 = form.cleaned_data['text2']
    form_text3 = form.cleaned_data['text3']
    form_text4 = form.cleaned_data['text4']
    form_changes = form.cleaned_data['changes']
    form_wwh = form.cleaned_data['what_why_how']
    class_model.objects.filter(user_id=user.id).update(
        text0=form_text0, 
        text1=form_text1, 
        text2=form_text2, 
        text3=form_text3, 
        text4=form_text4, 
        changes=form_changes, 
        what_why_how=form_wwh, 
        date_time=datetime.datetime.now()
        )


def add_parameter2_what_do_you_do(request): 
    user = User.objects.get(username=request.user)
    if request.method == 'POST':
        form = AddParameter2WhatDoYouDo(request.POST)
        if Parameter2WhatDoYouDo.objects.filter(user_id=user.id).exists():
            if form.is_valid():
                update_model(form, user, Parameter2WhatDoYouDo)
        else:
            if form.is_valid():
                save_taken_info(form, user)         
        return redirect('/what_do_you_do/')                   
    else:
        if Parameter2WhatDoYouDo.objects.filter(user_id=user.id).exists():
            model = Parameter2WhatDoYouDo.objects.get(user_id=user.id)
            form = AddParameter2WhatDoYouDo(instance=model)
            date_time = model.date_time
            return render(request, 'show.html', {'date_time':date_time, 'form':form})
        else:
            form = AddParameter2WhatDoYouDo()
            return render(request, 'questions.html', {'form':form})
            

def add_parameter3_environment(request): 
    user = User.objects.get(username=request.user)
    if request.method == 'POST':
        form = AddParameter3Environment(request.POST)
        if Parameter3Environment.objects.filter(user_id=user.id).exists():
            if form.is_valid():
                update_model(form, user, Parameter3Environment)
        else:
            if form.is_valid():
                save_taken_info(form, user)         
        return redirect('/environment/')                   
    else:
        if Parameter3Environment.objects.filter(user_id=user.id).exists():
            model = Parameter3Environment.objects.get(user_id=user.id)
            form = AddParameter3Environment(instance=model)
            date_time = model.date_time
            return render(request, 'show.html', {'date_time':date_time, 'form':form})
        else:
            form = AddParameter3Environment()
            return render(request, 'questions.html', {'form':form})


def add_parameter4_habits(request): 
    user = User.objects.get(username=request.user)
    if request.method == 'POST':
        form = AddParameter4Habits(request.POST)
        if Parameter4Habits.objects.filter(user_id=user.id).exists():
            if form.is_valid():
                update_model(form, user, Parameter4Habits)
        else:
            if form.is_valid():
                save_taken_info(form, user)         
        return redirect('/habits/')                   
    else:
        if Parameter4Habits.objects.filter(user_id=user.id).exists():
            model = Parameter4Habits.objects.get(user_id=user.id)
            form = AddParameter4Habits(instance=model)
            date_time = model.date_time
            return render(request, 'show.html', {'date_time':date_time, 'form':form})
        else:
            form = AddParameter4Habits()
            return render(request, 'questions.html', {'form':form})


def add_parameter5_free_time(request): 
    user = User.objects.get(username=request.user)
    if request.method == 'POST':
        form = AddParameter5FreeTime(request.POST)
        if Parameter5FreeTime.objects.filter(user_id=user.id).exists():
            if form.is_valid():
                update_model(form, user, Parameter5FreeTime)
        else:
            if form.is_valid():
                save_taken_info(form, user)         
        return redirect('/free_time/')                   
    else:
        if Parameter5FreeTime.objects.filter(user_id=user.id).exists():
            model = Parameter5FreeTime.objects.get(user_id=user.id)
            form = AddParameter5FreeTime(instance=model)
            date_time = model.date_time
            return render(request, 'show.html', {'date_time':date_time, 'form':form})
        else:
            form = AddParameter5FreeTime()
            return render(request, 'questions.html', {'form':form})    


def add_parameter6_appearance(request): 
    user = User.objects.get(username=request.user)
    if request.method == 'POST':
        form = AddParameter6Appearance(request.POST)
        if Parameter6Appearance.objects.filter(user_id=user.id).exists():
            if form.is_valid():
                update_model(form, user, Parameter6Appearance)
        else:
            if form.is_valid():
                save_taken_info(form, user)         
        return redirect('/appearance/')                   
    else:
        if Parameter6Appearance.objects.filter(user_id=user.id).exists():
            model = Parameter6Appearance.objects.get(user_id=user.id)
            form = AddParameter6Appearance(instance=model)
            date_time = model.date_time
            return render(request, 'show.html', {'date_time':date_time, 'form':form})
        else:
            form = AddParameter6Appearance()
            return render(request, 'questions.html', {'form':form})   

    
def add_parameter7_behavior(request): 
    user = User.objects.get(username=request.user)
    if request.method == 'POST':
        form = AddParameter7Behavior(request.POST)
        if Parameter7Behavior.objects.filter(user_id=user.id).exists():
            if form.is_valid():
                update_model(form, user, Parameter7Behavior)
        else:
            if form.is_valid():
                save_taken_info(form, user)         
        return redirect('/behavior/')                   
    else:
        if Parameter7Behavior.objects.filter(user_id=user.id).exists():
            model = Parameter7Behavior.objects.get(user_id=user.id)
            form = AddParameter7Behavior(instance=model)
            date_time = model.date_time
            return render(request, 'show.html', {'date_time':date_time, 'form':form})
        else:
            form = AddParameter7Behavior()
            return render(request, 'questions.html', {'form':form})  


def add_parameter8_mind(request): 
    user = User.objects.get(username=request.user)
    if request.method == 'POST':
        form = AddParameter8Mind(request.POST)
        if Parameter8Mind.objects.filter(user_id=user.id).exists():
            if form.is_valid():
                update_model(form, user, Parameter8Mind)
        else:
            if form.is_valid():
                save_taken_info(form, user)         
        return redirect('/mind/')                   
    else:
        if Parameter8Mind.objects.filter(user_id=user.id).exists():
            model = Parameter8Mind.objects.get(user_id=user.id)
            form = AddParameter8Mind(instance=model)
            date_time = model.date_time
            return render(request, 'show.html', {'date_time':date_time, 'form':form})
        else:
            form = AddParameter8Mind()
            return render(request, 'questions.html', {'form':form}) 


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