from django import forms
from .models import *

from django.contrib.auth.models import User
from .models import Profile


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [ 'title', 'description', 'tipo', 'complete'] 

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Título da Tarefa'}),
            'description':forms.Textarea(attrs={'cols':20, 'rows': 6, 'class':'form-control', 'placeholder':'Sobre a sua tarefa...' }),
            'complete':forms.CheckboxInput(attrs={'class':'form-control', 'class':'mail-choice', 'type': 'checkbox', 'name':'msg', 'for':'mail30' }),
                
            }
        labels = {
            'title': 'Título',
            'description': 'Descrição',
            'complete': 'Status da tarefa'
        }


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email']
        
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
        