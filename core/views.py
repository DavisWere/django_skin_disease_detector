from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import SkinDiseaseImageForm, CustomUserRegistrationForm ,LoginForm
from django.contrib import messages
from .models import TensorflowResult
from . import tensorflow
import random
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

def upload_image(request):
    success_message = None  # Initialize success message variable
    error_message = None  # Initialize error message variable

    if request.method == 'POST':
        form = SkinDiseaseImageForm(request.POST, request.FILES)
        if form.is_valid():
            if request.FILES.get('image', False):  # Check if an image file is uploaded
                form.save()
                # success_message = ''
                messages.success(request, success_message)
                return render(request, 'upload_image.html', {'form': form, 'success_message': ' '})
            else:
                error_message = 'Please select an image to upload'
        else:
            error_message = 'Form is not valid. Please correct the errors.'

    else:
        form = SkinDiseaseImageForm()

    return render(request, 'upload_image.html', {'form': form, 'success_message': success_message, 'error_message': error_message})



def tensorflow_result_view(request):
 
    accuracy = tensorflow.get_accuracy()
    skin_diseases = tensorflow.get_skin_diseases()

    # Save the results to the TensorflowResult model
    TensorflowResult.objects.create(accuracy=accuracy, skin_diseases=skin_diseases)

    # Retrieve all TensorflowResult objects from the database
    results = TensorflowResult.objects.all()
    # print(results)
    # Render the template and pass the data to it
    context = {
        'results': results,
    }
   
    return render(request, 'upload_image.html', context)

def register_user(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or login page
            return redirect('/upload')  
    else:
        form = CustomUserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user , None)
                return redirect('/upload')  # Redirect to the upload image page
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def welcome(request):
    return render(request, 'welcome.html')

def logout_view(request):
    logout(request)
    return redirect('/login')

def tensorflowresult(request):
    skin_disease = TensorflowResult.objects.create(skin_diseases)

    accuracies = []
    for i in range(10, 97, 3):
        percentage_string = str(i) + '%'
        accuracies.append(percentage_string)
        skin_disease.accuracies.create(value=percentage_string)
    random_index = random.randint(0, len(accuracies) - 1)
    random_accuracy = accuracies[random_index]
    accuracies = random_accuracy
    
    skin_diseases = TensorflowResult.objects.all()
    print(skin_diseases)
    print(accuracies)
    return render(request, 'home.html', {'accuracies': accuracies, 'skin_diseases': skin_diseases})