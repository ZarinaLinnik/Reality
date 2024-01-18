from django import forms
from .models import Parameter1WhoAreYou, ParameterIMGMyPhoto


class AddParameter1WhoAreYou(forms.ModelForm):

    class Meta:
        model = Parameter1WhoAreYou
        fields = ('name', 'surname', 'goals', 'changes', 'what_why_how')
        exlude = ('date_time', 'user')
        labels = {'name':'Name', 'surname':'Surname', 'goals':'Your goals', 'changes':'What do you want to change from this list', 'what_why_how':'What-Why-How are going to do that?'}
        widgets = {'goals':forms.Textarea(), 'changes':forms.Textarea(), 'what_why_how':forms.Textarea(),}


class AddParameterIMGMyPhoto(forms.ModelForm):

    class Meta:
        model = ParameterIMGMyPhoto
        fields = ('image',)


class GiveFeedBack(forms.Form):
    title = forms.CharField(max_length=200, min_length=2, required=True, label='Title')
    text = forms.CharField(widget=forms.Textarea(), label='Feedback from you')