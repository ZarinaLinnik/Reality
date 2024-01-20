from django import forms
from .models import ParameterIMGMyPhoto, Parameter1WhoAreYou, Parameter2WhatDoYouDo


    # class Meta:
    #     model = ...
    #     fields = ('...', 'changes', 'what_why_how')
    #     exlude = ('date_time', 'user')
    #     labels = {'...':'...', 'changes':'What do you want to change from this list', 'what_why_how':'What-Why-How are going to achieve that?'}


class GiveFeedBack(forms.Form):
    email = forms.EmailField(label='Your email')
    subject = forms.CharField(max_length=200, min_length=2, required=True, label='Subject')
    message = forms.CharField(widget=forms.Textarea(), label='Message')


class AddParameterIMGMyPhoto(forms.ModelForm):

    class Meta:
        model = ParameterIMGMyPhoto
        fields = ('image', 'date_time_pict',)


class AddParameter1WhoAreYou(forms.ModelForm):

    class Meta:
        model = Parameter1WhoAreYou
        fields = ('name', 'surname', 'goals', 'changes', 'what_why_how')
        exlude = ('date_time', 'user')
        labels = {
            'name':'Name',
            'surname':'Surname', 
            'goals':'Your goals', 
            'changes':'What do you want to change from this list', 
            'what_why_how':'What-Why-How are going to achieve that?'
            }


class AddParameter2WhatDoYouDo(forms.ModelForm): 

    class Meta:
        model = Parameter2WhatDoYouDo
        fields = ('text1', 'text2', 'text3', 'text4', 'changes', 'what_why_how')
        exlude = ('date_time', 'user')
        labels = {
            'text1':'How do you prioritize and manage your tasks?',
            'text2':'Are there any specific challenges or goals you are currently working on?', 
            'text3':'How do you balance your work/study with other aspects of your life?', 
            'text4':'Do you have any strategies or routines that help you stay organized and productive?', 
            'changes':'What do you want to change from this list', 
            'what_why_how':'What-Why-How are going to achieve that?',
            }


class AddParameter3Environment(forms.ModelForm): pass
class AddParameter4Habits(forms.ModelForm): pass
class AddParameter5FreeTime(forms.ModelForm): pass
class AddParameter6LookLike(forms.ModelForm): pass
class AddParameter7Behavior(forms.ModelForm): pass
class AddParameter8ThoughtsDirection(forms.ModelForm): pass
