from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import SkinDiseaseImage, CustomUser

class SkinDiseaseImageForm(forms.ModelForm):
    class Meta:
        model = SkinDiseaseImage
        fields = ['image']
    
    
class CustomUserRegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password', 'location', 'phone_number']
    

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'px-4 py-2 border-b rounded', 'placeholder': 'Enter your username'})
        self.fields['password'].widget.attrs.update({'class': 'px-4 py-2 border-b rounded', 'placeholder': 'Enter your password'})