from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        # UserCreationForm.Meta.fields ni ishlatmaymiz, 
        # chunki u yerda biz o'chirib tashlagan 'username' bor.
        fields = ('phone_number', 'first_name', 'last_name', 'birth_date', 'profile_picture')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        # Bu yerda ham 'username' bo'lmasligi kerak
        fields = ('phone_number', 'first_name', 'last_name', 'birth_date', 'profile_picture', 'email')