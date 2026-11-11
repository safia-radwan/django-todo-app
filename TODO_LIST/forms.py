from django import forms
from .models import tasks
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



        
class date_Form(forms.ModelForm):
    class Meta:
        model = tasks
        fields = ['task','due_date','priority','catigory']
        
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'})
            }
        
        
class register_from(UserCreationForm):
    email=forms.EmailField(required=True)
    class Meta:
        model=User
        fields = ['username', 'email','password1','password2']
    

