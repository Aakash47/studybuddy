from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models as user_model

class CreateUserForm(UserCreationForm):

    class Meta:
        model = user_model.Userprofile
        fields = ['first_name','last_name','email','username', "password1", "password2",'ucourse','ucollege']
        help_texts = {
            'username':None,
        }