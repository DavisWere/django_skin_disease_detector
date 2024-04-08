from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import reverse

app_name = 'core'

urlpatterns = [
    path('upload/success/', views.upload_image, name='upload_success'),
    path('register/',views.register_user, name='registration'),
    path('login/',views.login_view, name='login'),
    path('',views.welcome, name='welcome'),
    path('image/', views.skin_disease_image_view, name='last_uploaded_image'),
    path('logout/',views.logout_view, name='logout'),
    path('excel-report/',views.generate_excel_file, name= 'generate_excel_file'),
    path('pdf-report/', views.generate_pdf_report, name='pdf report for scanned skin diseases'),
    path('upload/', views.upload_image, name='upload_image'),
    path('geolocation/', views.find_nearest_hospitals, name='find_nearest_hospitals'),
    path('hospital-data/', views.hospital_data, name='hospital data'),
    path('admin-dashboard/',views.display_data, name = 'data report'),  # for admin dashboard

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# 