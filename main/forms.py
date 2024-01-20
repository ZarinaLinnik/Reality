from django import forms
from .models import Parameter1WhoAreYou, ParameterIMGMyPhoto


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
        labels = {'name':'Name', 'surname':'Surname', 'goals':'Your goals', 'changes':'What do you want to change from this list', 'what_why_how':'What-Why-How are going to achieve that?'}
        widgets = {'goals':forms.Textarea(), 'changes':forms.Textarea(), 'what_why_how':forms.Textarea(),}


class AddParameter2WhatDoYouDo(forms.ModelForm): pass
class AddParameter3Environment(forms.ModelForm): pass
class AddParameter4Habits(forms.ModelForm): pass
class AddParameter5FreeTime(forms.ModelForm): pass
class AddParameter6LookLike(forms.ModelForm): pass
class AddParameter7Behavior(forms.ModelForm): pass
class AddParameter8ThoughtsDirection(forms.ModelForm): pass
