from django.contrib import admin

from .models import SkinDiseaseImage, CustomUser, TensorflowResult, Hospital, History

admin.site.register(SkinDiseaseImage)
admin.site.register(CustomUser)
admin.site.register(TensorflowResult)
admin.site.register(Hospital)
admin.site.register(History)