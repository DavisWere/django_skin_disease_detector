from django.contrib import admin

from .models import SkinDiseaseImage, CustomUser, TensorflowResult, Hospital

admin.site.register(SkinDiseaseImage)
admin.site.register(CustomUser)
admin.site.register(TensorflowResult)
admin.site.register(Hospital)