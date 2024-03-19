from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'core'

urlpatterns = [
    path('upload/', views.upload_image, name='upload_image'),
    path('upload/success/', views.upload_image, name='upload_success'),
    path('register/',views.register_user, name='registration'),
    path('login/',views.login_view, name='login'),
    # path('custom-login/',views.custom_login_view, name='custom_login'),
    path('',views.welcome, name='welcome'),
    path('image/', views.skin_disease_image_view, name='last_uploaded_image'),
    # path('image',views.image_render, name='image'),
    # path('image/', views.display_skin_disease_image_by_id, name='image_detail'),
    # path('image/<int:id>/', views.skin_disease_image_view, name='skin_disease_image'),
    # path('image/<int:image_id>/', views.display_skin_disease_image_by_id, name='image_detail'),
    path('logout/',views.logout_view, name='logout'),
    path('excel-report/',views.generate_excel_file, name= 'generate_excel_file'),
    path('pdf-report/', views.generate_pdf, name='generate_pdf')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)