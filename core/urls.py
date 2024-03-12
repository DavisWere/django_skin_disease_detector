from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('upload/', views.upload_image, name='upload_image'),
    path('upload/success/', views.upload_image, name='upload_success'),
]