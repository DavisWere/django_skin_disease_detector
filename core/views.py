from django.shortcuts import render, redirect
from .forms import SkinDiseaseImageForm

def upload_image(request):
    if request.method == 'POST':
        form = SkinDiseaseImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_success')
    else:
        form = SkinDiseaseImageForm()
    return render(request, 'upload_image.html', {'form': form})

def upload_success(request):
    return render(request, 'upload_success.html')
