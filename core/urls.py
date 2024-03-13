from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('upload/', views.upload_image, name='upload_image'),
    path('upload/success/', views.upload_image, name='upload_success'),
    path('register/',views.register_user, name='registration'),
    path('login/',views.login_view, name='login'),
    # path('custom-login/',views.custom_login_view, name='custom_login'),
    path('/',views.welcome, name='welcome'),
    path('logout/',views.logout_view, name='logout'),
    path('excel-report/',views.generate_excel_file, name= 'generate_excel_file'),
    path('pdf-report/', views.generate_pdf, name='generate_pdf')

]