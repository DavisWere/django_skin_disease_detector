from django.db import models
from django.contrib.auth.models import AbstractUser

class SkinDiseaseImage(models.Model):
    image = models.ImageField(upload_to='skin_disease_images/')