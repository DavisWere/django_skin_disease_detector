from django.db import models

import os
from datetime import datetime
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.validators import RegexValidator
from django.utils import timezone

phone_validator = RegexValidator(r"^\d{9,10}$", "Enter a valid phone number.")

phone_code_validator = RegexValidator(r"^\+\d{1,3}$")

class CustomUser(models.Model):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length = 128, unique =True,  default = 'admin')
    password = models.CharField(max_length=128, default='123456')
    phone_number= models.CharField(max_length= 20, blank=True, null=True)
    
    location = models.CharField(max_length = 128, blank=True, null=True)
    def __str__(self):
        return self.username

class SkinDiseaseImage(models.Model):
    image = models.ImageField(upload_to='skin_disease_images/')

class TensorflowResult(models.Model):
    accuracy = models.CharField(max_length= 4, blank=False, null= False)
    skin_diseases = models.CharField(max_length=30, blank= True, null= True)

    def __str__(self):
        return f"Disease: {self.skin_diseases}, Accuracy: {self.accuracy}"