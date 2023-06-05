from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
 
class createuserform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password'] 
 
class addAlumnus(ModelForm):
    class Meta:
        model=Alumni
        fields= '__all__'

class editAlumnus(ModelForm):
    class Meta:
        model=Alumni
        fields= '__all__'

