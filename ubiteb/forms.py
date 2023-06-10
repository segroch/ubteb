from django import forms
from django.forms import ModelForm

from ubiteb.utils import get_centers_from_csv
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .utils import *

# Rest of your code...


class createuserform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class addAlumnus(forms.ModelForm):
    #exam_centers = forms.TypedChoiceField(choices=(), coerce=str)

    #disrticts = forms.TypedChoiceField(choices=(), coerce=str)
        
    #progrms = forms.TypedChoiceField(choices=(), coerce=str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Set the choices for the exam_centers field
        self.fields['exam_center'].choices = get_centers_from_csv('ubiteb/examCenters.csv')
        self.fields['program'].choices = get_programs_from_csv('ubiteb/programs.csv')
        self.fields['district'].choices = get_districts_from_csv('ubiteb/districts.csv')
        
        # Set up crispy forms helper
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))
        


    class Meta:
        model = Alumni
        fields = '__all__'
    


class editAlumnus(ModelForm):
    class Meta:
        model = Alumni
        fields = '__all__'
