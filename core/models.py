from django.db import models
class SkinDiseaseImage(models.Model):
    image = models.ImageField(upload_to='skin_disease_images/')