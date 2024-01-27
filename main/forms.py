from django import forms
from .models import (
    ParameterIMGMyPhoto, 
    Parameter1WhoAreYou, 
    Parameter2WhatDoYouDo, 
    Parameter3Environment, 
    Parameter4Habits, 
    Parameter5FreeTime, 
    Parameter6Appearance, 
    Parameter7Behavior, 
    Parameter8Mind
    )

'''
    class Meta:
        model = ...
        fields = ('text0', '...', 'changes', 'what_why_how')
        exlude = ('date_time', 'user')
        labels = {
            'text0':'main_question',
            '...':'...', 
            'changes':'What do you want to change from this list', 
            'what_why_how':'What-Why-How are going to achieve that?'}
'''


class GiveFeedBack(forms.Form):
    email = forms.EmailField(label='Your email')
    subject = forms.CharField(max_length=200, min_length=2, required=True, label='Subject')
    message = forms.CharField(widget=forms.Textarea(), label='Message')


class AddParameterIMGMyPhoto(forms.ModelForm):

    class Meta:
        model = ParameterIMGMyPhoto
        fields = ('image', 'date_time_pict',)
        errors = {'date_time_pict':'Input the correct date&time'}
        widgets = {
            'date_time_pict':forms.DateTimeInput(
                {
                    'pattern':r'^\d{2}/\d{2}/\d{4} \d{2}:\d{2}$', 
                    'title': 'Pattern: MM/DD/YYYY HH:MM',
                    'placeholder':'__/__/____ __:__',
                    'maxlength':'16',
                }, 
                format='%m/%d/%Y %H:%M'),
            }


class AddParameter1WhoAreYou(forms.ModelForm):

    class Meta:
        model = Parameter1WhoAreYou
        fields = ('text0', 'name', 'surname', 'goals', 'changes', 'what_why_how')
        exclude = ('date_time', 'user')
        labels = {
            'text0':'Who are you? What do you want from this life and from you?',
            'name':'What is your name?',
            'surname':'What is your surname?', 
            'goals':'What are your goals', 
            'changes':'What do you want to change from this list', 
            'what_why_how':'What-Why-How are going to achieve that?',
            }


class AddParameter2WhatDoYouDo(forms.ModelForm): 

    class Meta:
        model = Parameter2WhatDoYouDo
        fields = ('text0', 'text1', 'text2', 'text3', 'text4', 'changes', 'what_why_how')
        exclude = ('date_time', 'user')
        labels = {
            'text0':'What do you do every week? (work, study, housework)',
            'text1':'How do you prioritize and manage your tasks?',
            'text2':'Are there any specific challenges or goals you are currently working on?', 
            'text3':'How do you balance your work/study with other aspects of your life?', 
            'text4':'Do you have any strategies or routines that help you stay organized and productive?', 
            'changes':'What do you want to change from this list', 
            'what_why_how':'What-Why-How are going to achieve that?',
            }


class AddParameter3Environment(forms.ModelForm): 
    
    class Meta:
        model = Parameter3Environment
        fields = ('text0', 'text1', 'text2', 'text3', 'text4', 'changes', 'what_why_how')
        exclude = ('date_time', 'user')
        labels = {
            'text0':'What does your room or environment look like?',
            'text1':'What is the overall atmosphere or vibe of your room?',
            'text2':'What objects or decorations are present that reflect your personality or interests?', 
            'text3':'How do you keep your room organized and clean?', 
            'text4':'Is there anything specific in your room that you find particularly special or meaningful?', 
            'changes':'What do you want to change from this list', 
            'what_why_how':'What-Why-How are going to achieve that?',
            }
        

class AddParameter4Habits(forms.ModelForm): 
        
    class Meta:
        model = Parameter4Habits
        fields = ('text0', 'text1', 'text2', 'text3', 'text4', 'changes', 'what_why_how')
        exclude = ('date_time', 'user')
        labels = {
            'text0':'What are your habits?',
            'text1':'Are there any habits that you find particularly beneficial or important?',
            'text2':'Do you have any habits that you would like to change or improve?', 
            'text3':'How do your habits contribute to your overall well-being or productivity?', 
            'text4':'Have your habits evolved or changed over time?', 
            'changes':'What do you want to change from this list', 
            'what_why_how':'What-Why-How are going to achieve that?',
            }
        

class AddParameter5FreeTime(forms.ModelForm): 
        
    class Meta:
        model = Parameter5FreeTime
        fields = ('text0', 'text1', 'text2', 'text3', 'text4', 'changes', 'what_why_how')
        exclude = ('date_time', 'user')
        labels = {
            'text0':'How do you spend your free time?',
            'text1':'What activities or hobbies do you enjoy during your leisure hours?',
            'text2':'Do you prefer to spend your free time alone or with others?', 
            'text3':'How do you find a balance between relaxation and pursuing your interests?', 
            'text4':'Are there any specific activities that you would like to explore in your free time?', 
            'changes':'What do you want to change from this list', 
            'what_why_how':'What-Why-How are going to achieve that?',
            }
        
        
class AddParameter6Appearance(forms.ModelForm): 
        
    class Meta:
        model = Parameter6Appearance
        fields = ('text0', 'text1', 'text2', 'text3', 'text4', 'changes', 'what_why_how')
        exclude = ('date_time', 'user')
        labels = {
            'text0':'What do you look like?',
            'text1':'What physical features do you find unique or distinctive about yourself?',
            'text2':'How do you typically dress or present yourself to others?', 
            'text3':'Do you have any specific grooming routines or practices?', 
            'text4':'How does your appearance contribute to your overall self-image or confidence?', 
            'changes':'What do you want to change from this list', 
            'what_why_how':'What-Why-How are going to achieve that?',
            }
        

class AddParameter7Behavior(forms.ModelForm): 
        
    class Meta:
        model = Parameter7Behavior
        fields = ('text0', 'text1', 'text2', 'text3', 'text4', 'changes', 'what_why_how')
        exclude = ('date_time', 'user')
        labels = {
            'text0':'What is your behavior like?',
            'text1':'Are you generally extroverted, introverted, or somewhere in between?',
            'text2':'How do you interact with others in social settings?', 
            'text3':'Do you have any behavioral patterns or tendencies that you are aware of?', 
            'text4':'How would you describe your overall demeanor or temperament?', 
            'changes':'What do you want to change from this list', 
            'what_why_how':'What-Why-How are going to achieve that?',
            }
        

class AddParameter8Mind(forms.ModelForm): 
        
    class Meta:
        model = Parameter8Mind
        fields = ('text0', 'text1', 'text2', 'text3', 'text4', 'changes', 'what_why_how')
        exclude = ('date_time', 'user')
        labels = {
            'text0':'How do you think?',
            'text1':'Are you more analytical or intuitive in your thinking process?',
            'text2':'Do you prefer to think things through methodically or rely on your instincts?', 
            'text3':'Are there any specific thinking strategies or techniques that you employ?', 
            'text4':'How do you handle challenges or conflicts that require critical thinking?', 
            'changes':'What do you want to change from this list', 
            'what_why_how':'What-Why-How are going to achieve that?',
            }
        
