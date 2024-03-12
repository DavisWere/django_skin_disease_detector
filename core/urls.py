from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('upload/', views.upload_image, name='upload_image'),
    path('upload/success/', views.upload_image, name='upload_success'),
    path('register/',views.register_user, name='registration'),
    path('login/',views.login_view, name='login')
]