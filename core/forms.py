from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import SkinDiseaseImage, CustomUser 

class SkinDiseaseImageForm(forms.ModelForm):
    class Meta:
        model = SkinDiseaseImage
        fields = ['image']
    
    

class CustomUserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=20, required=False)
    location = forms.CharField(max_length=128, required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'phone_number', 'location']
        
class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'px-4 py-2 border-b rounded', 'placeholder': 'Enter your username'})
        self.fields['password'].widget.attrs.update({'class': 'px-4 py-2 border-b rounded', 'placeholder': 'Enter your password'})

# class LoginForm(forms.Form):
#     username = forms.CharField(max_length=128)
#     password = forms.CharField(widget=forms.PasswordInput)

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['username'].widget.attrs.update({'class': 'px-4 py-2 border-b rounded', 'placeholder': 'Enter your username', 'required': 'required'})
#         self.fields['password'].widget.attrs.update({'class': 'px-4 py-2 border-b rounded', 'placeholder': 'Enter your password', 'required': 'required'})