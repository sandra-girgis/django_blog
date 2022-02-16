from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class UserForm(UserCreationForm):
    class Meta:
        is_staff = forms.BooleanField(required=True, initial=True)
        model = User
        fields = ('username', 'email', 'password1','password2','is_staff')
        
        # widget = {
        #     'is_staff': forms.BooleanField(initial=True)
        # }
        # fields = ('__all__')
    



