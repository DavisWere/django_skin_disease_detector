from django import forms
from .models import SkinDiseaseImage

class SkinDiseaseImageForm(forms.ModelForm):
    class Meta:
        model = SkinDiseaseImage
        fields = ['image']