from django.shortcuts import render, redirect

from .forms import SkinDiseaseImageForm
from django.contrib import messages

def upload_image(request):
    success_message = None  # Initialize success message variable
    error_message = None  # Initialize error message variable

    if request.method == 'POST':
        form = SkinDiseaseImageForm(request.POST, request.FILES)
        if form.is_valid():
            if request.FILES.get('image', False):  # Check if an image file is uploaded
                form.save()
                success_message = 'Image uploaded successfully'
                messages.success(request, success_message)
                return render(request, 'upload_image.html', {'form': form, 'success_message': success_message})
            else:
                error_message = 'Please select an image to upload'
        else:
            error_message = 'Form is not valid. Please correct the errors.'

    else:
        form = SkinDiseaseImageForm()

    return render(request, 'upload_image.html', {'form': form, 'success_message': success_message, 'error_message': error_message})