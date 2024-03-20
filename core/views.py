from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from .forms import SkinDiseaseImageForm, CustomUserRegistrationForm ,LoginForm
from django.contrib import messages
from .models import TensorflowResult, SkinDiseaseImage
from .forms import LoginForm
import pandas as pd
import openpyxl 
from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference
from openpyxl.styles import PatternFill
from openpyxl.drawing.colors import ColorChoice
from io import BytesIO
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from django.http import HttpResponse
import random
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

ACNE = 'Acne'
ECZEMA = 'Eczema (Dermatitis)'
PSORIASIS = 'Psoriasis'
ROSACEA = 'Rosacea'
DERMATITIS_HERPETIFORMIS = 'Dermatitis Herpetiformis'
SKIN_CANCER = 'Skin Cancer'
HIVES = 'Hives (Urticaria)'
VITILIGO = 'Vitiligo'
FUNGAL_INFECTIONS = 'Fungal Infections'
SCABIES = 'Scabies'
ATOPIC_DERMATITIS = 'Atopic Dermatitis'
CONTACT_DERMATITIS = 'Contact Dermatitis'
SEBORRHEIC_DERMATITIS = 'Seborrheic Dermatitis'
ACTINIC_KERATOSIS = 'Actinic Keratosis'
BASAL_CELL_CARCINOMA = 'Basal Cell Carcinoma'
SQUAMOUS_CELL_CARCINOMA = 'Squamous Cell Carcinoma'
MELANOMA = 'Melanoma'
KERATOSIS_PILARIS = 'Keratosis Pilaris'
LICHEN_PLANUS = 'Lichen Planus'
PITIRIASIS_ROSEA = 'Pityriasis Rosea'
TINEA_VERSICOLOR = 'Tinea Versicolor'
IMPETIGO = 'Impetigo'
CELLULITIS = 'Cellulitis'
MOLLUSCUM_CONTAGIOSUM = 'Molluscum Contagiosum'
WARTS = 'Warts'
HIDRADENITIS_SUPPURATIVA = 'Hidradenitis Suppurativa'
ICHTHYOSIS = 'Ichthyosis'
FOLLICULITIS = 'Folliculitis'
PERIORAL_DERMATITIS = 'Perioral Dermatitis'
DYSHIDROTIC_ECZEMA = 'Dyshidrotic Eczema'
GRANULOMA_ANNULARE = 'Granuloma Annulare'
LUPUS = 'Lupus'
SCLERODERMA = 'Scleroderma'
EPIDERMOLYSIS_BULLOSA = 'Epidermolysis Bullosa'
PRURIGO_NODULARIS = 'Prurigo Nodularis'
PEMPHIGUS = 'Pemphigus'
PEMPHIGOID = 'Pemphigoid'
MORBILLIFORM_DRUG_ERUPTION = 'Morbilliform Drug Eruption'
STEVENS_JOHNSON_SYNDROME = 'Stevens-Johnson Syndrome'
TOXIC_EPIDERMAL_NECROLYSIS = 'Toxic Epidermal Necrolysis'
ERYTHEMA_MULTIFORME = 'Erythema Multiforme'
CUTANEOUS_T_CELL_LYMPHOMA = 'Cutaneous T-cell Lymphoma'
KAPOSI_S_SARCOMA = 'Kaposis Sarcoma'
PYODERMA_GANGRENOSUM = 'Pyoderma Gangrenosum'
EOSINOPHILIC_PUSTULAR_FOLLICULITIS = 'Eosinophilic Pustular Folliculitis'
NECROBIOSIS_LIPOIDICA = 'Necrobiosis Lipoidica'
SWEET_S_SYNDROME = "Sweet's Syndrome"
LICHEN_SCLEROSUS = 'Lichen Sclerosus'
PRURITUS = 'Pruritus'
XEROSIS = 'Xerosis'
ONYCHOMYCOSIS = 'Onychomycosis'
PILONIDAL_CYST = 'Pilonidal Cyst'
LIPOMA = 'Lipoma'
SEBACEOUS_CYST = 'Sebaceous Cyst'
KELOIDS = 'Keloids'
ANGIOMAS = 'Angiomas'
DERMATOFIBROMA = 'Dermatofibroma'
NODISEASE = 'no known disease'  

DISEASE_CHOICES = [
(ACNE, ACNE),
(ECZEMA, ECZEMA),
(PSORIASIS, PSORIASIS),
(ROSACEA, ROSACEA),
(DERMATITIS_HERPETIFORMIS, DERMATITIS_HERPETIFORMIS),
(SKIN_CANCER, SKIN_CANCER),
(HIVES, HIVES),
(VITILIGO, VITILIGO),
(FUNGAL_INFECTIONS, FUNGAL_INFECTIONS),
(SCABIES, SCABIES),
(ATOPIC_DERMATITIS, ATOPIC_DERMATITIS),
(CONTACT_DERMATITIS, CONTACT_DERMATITIS),
    (SEBORRHEIC_DERMATITIS, 'Seborrheic Dermatitis'),
(ACTINIC_KERATOSIS, 'Actinic Keratosis'),
(BASAL_CELL_CARCINOMA, 'Basal Cell Carcinoma'),
(SQUAMOUS_CELL_CARCINOMA, 'Squamous Cell Carcinoma'),
(MELANOMA, 'Melanoma'),
(KERATOSIS_PILARIS, 'Keratosis Pilaris'),
(LICHEN_PLANUS, 'Lichen Planus'),
(PITIRIASIS_ROSEA, 'Pityriasis Rosea'),
(TINEA_VERSICOLOR, 'Tinea Versicolor'),
(IMPETIGO, 'Impetigo'),
(CELLULITIS, 'Cellulitis'),
(MOLLUSCUM_CONTAGIOSUM, 'Molluscum Contagiosum'),
(WARTS, 'Warts'),
(HIDRADENITIS_SUPPURATIVA, 'Hidradenitis Suppurativa'),
(ICHTHYOSIS, 'Ichthyosis'),
(FOLLICULITIS, 'Folliculitis'),
(PERIORAL_DERMATITIS, 'Perioral Dermatitis'),
(DYSHIDROTIC_ECZEMA, 'Dyshidrotic Eczema'),
(GRANULOMA_ANNULARE, 'Granuloma Annulare'),
(LUPUS, 'Lupus'),
(SCLERODERMA, 'Scleroderma'),
(EPIDERMOLYSIS_BULLOSA, 'Epidermolysis Bullosa'),
(PRURIGO_NODULARIS, 'Prurigo Nodularis'),
(PEMPHIGUS, 'Pemphigus'),
(PEMPHIGOID, 'Pemphigoid'),
(MORBILLIFORM_DRUG_ERUPTION, 'Morbilliform Drug Eruption'),
(STEVENS_JOHNSON_SYNDROME, 'Stevens-Johnson Syndrome'),
(TOXIC_EPIDERMAL_NECROLYSIS, 'Toxic Epidermal Necrolysis'),
(ERYTHEMA_MULTIFORME, 'Erythema Multiforme'),
(CUTANEOUS_T_CELL_LYMPHOMA, 'Cutaneous T-cell Lymphoma'),
(KAPOSI_S_SARCOMA, "Kaposi's Sarcoma"),
(PYODERMA_GANGRENOSUM, 'Pyoderma Gangrenosum'),
(EOSINOPHILIC_PUSTULAR_FOLLICULITIS, 'Eosinophilic Pustular Folliculitis'),
(NECROBIOSIS_LIPOIDICA, 'Necrobiosis Lipoidica'),
(SWEET_S_SYNDROME, "Sweet's Syndrome"),
(LICHEN_SCLEROSUS, 'Lichen Sclerosus'),
(PRURITUS, 'Pruritus'),
(XEROSIS, 'Xerosis'),
(ONYCHOMYCOSIS, 'Onychomycosis'),
(PILONIDAL_CYST, 'Pilonidal Cyst'),
(LIPOMA, 'Lipoma'),
(SEBACEOUS_CYST, 'Sebaceous Cyst'),
(KELOIDS, 'Keloids'),
(ANGIOMAS, 'Angiomas'),
(DERMATOFIBROMA, 'Dermatofibroma')]



def generate_data():
   
    skin_diseases = [disease[0] for disease in DISEASE_CHOICES]

    
    random_disease_index = random.randint(0, len(skin_diseases) - 1)
    random_disease = skin_diseases[random_disease_index]

    accuracies = []
    for i in range(10, 97, 3):
        percentage_string = str(i) + '%'
        accuracies.append(percentage_string)

    random_accuracy_index = random.randint(0, len(accuracies) - 1)
    random_accuracy = accuracies[random_accuracy_index]
   
    return random_disease, random_accuracy
    

def insert_data_into_database():
 
    random_disease, random_accuracy = generate_data()
    
    # Print the random disease and accuracy to debug
    # print(" Disease:", random_disease)
    # print("Accuracy:", random_accuracy)

    # Create a TensorflowResult instance with the random disease and accuracy
    result = TensorflowResult.objects.create(skin_diseases=random_disease, accuracy=random_accuracy)
    # print("Created TensorflowResult:", result)


def generate_excel_file(request):
    # Query the database to retrieve all TensorflowResult objects
    results = TensorflowResult.objects.all()

    # Create a DataFrame to store the data
    data = {'Skin Disease': [], 'Accuracy': []}

    # Populate the DataFrame with data from the database
    for result in results:
        data['Skin Disease'].append(result.skin_diseases)
        data['Accuracy'].append(result.accuracy)

    # Convert the DataFrame to a pandas DataFrame
    df = pd.DataFrame(data)

    # Write the DataFrame to an Excel file
    file_path = 'skin_disease_results.xlsx'
    df.to_excel(file_path, index=False)

    # Create a workbook and load the Excel file
    wb = openpyxl.load_workbook(file_path)
    ws = wb.active

    # Create a bar chart using the data in the Excel file
    chart = BarChart()
    chart.title = "Skin Disease Accuracy"
    chart.x_axis.title = "Skin Disease"
    chart.y_axis.title = "Accuracy (%)"

    values = Reference(ws, min_col=2, min_row=2, max_col=2, max_row=len(df) + 1)
    categories = Reference(ws, min_col=1, min_row=2, max_row=len(df) + 1)
    chart.add_data(values, titles_from_data=True)
    chart.set_categories(categories)

    # Set chart colors
    chart_colors = ['medSeaGreen', 'cornflowerBlue', 'papayaWhip', 'plum', 'medAquamarine']  # Example colors
    for idx, s in enumerate(chart.series):
        fill = openpyxl.drawing.colors.ColorChoice(prstClr=chart_colors[idx])
        s.graphicalProperties.solidFill = fill

    # Add the chart to the worksheet
    ws.add_chart(chart, "D1")

    # Save the workbook
    wb.save(file_path)

    # Open the file and read its content
    with open(file_path, 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=skin_disease_results.xlsx'

    return response
def generate_pdf(request):
    # Query the database to retrieve all TensorflowResult objects
    results = TensorflowResult.objects.all()

    # Create data for the PDF table
    data = [['Skin Disease', 'Accuracy']]

    # Populate the data with values from the database
    for result in results:
        data.append([result.skin_diseases, result.accuracy])

    # Create a buffer for the PDF
    buffer = BytesIO()

    # Create a PDF document
    pdf = SimpleDocTemplate(buffer, pagesize=letter)
    
    # Create a table
    table = Table(data)

    # Style the table
    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black)])

    # Apply the table style
    table.setStyle(style)

    # Add table to the PDF
    pdf.build([table])

    # Get PDF content from buffer
    pdf_content = buffer.getvalue()
    buffer.close()

    # Create a HTTP response with the PDF content
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=skin_disease_results.pdf'
    response.write(pdf_content)

    return response

def skin_disease_image_view(request):
    # Get the last uploaded image based on the order of insertion (last object in the database)
    last_uploaded_image = SkinDiseaseImage.objects.last()
    
    # Check if any images exist in the database
    if last_uploaded_image is not None:
        context = {'image': last_uploaded_image}
        return render(request, 'upload_image.html', context)
    else:
        # Handle the case where no images are found
        return render(request, 'no_images.html')

def upload_image(request):
    success_message = None  # Initialize success message variable
    error_message = None  # Initialize error message variable

    if request.method == 'POST':
        form = SkinDiseaseImageForm(request.POST, request.FILES)
        
        if form.is_valid():
            if request.FILES.get('image', False):  # Check if an image file is uploaded
                form.save()
                # success_message = ''
                
                insert_data_into_database()
                messages.success(request, success_message)
                latest_result = TensorflowResult.objects.last()

                context = {'latest_result': latest_result}
                last_uploaded_image = SkinDiseaseImage.objects.last()
    
    # Check if any images exist in the database
                if last_uploaded_image is not None:
                    context = {'latest_result':latest_result,'image': last_uploaded_image}
                    return render(request, 'upload_image.html', context)
                else:
                    # Handle the case where no images are found
                    return render(request, 'no_images.html')
                
                
                # return render(request, 'upload_image.html', context)
                
            else:
                error_message = 'Please select an image to upload'
        else:
            error_message = 'Form is not valid. Please correct the errors.'

    else:
        
        form = SkinDiseaseImageForm()
        skin_disease_image_view(request)

    return render(request, 'upload_image.html', {'form': form, 'success_message': success_message, 'error_message': error_message})










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
                login(request, user)
                return redirect('/upload')  # Redirect to the upload image page
            else:
                # Invalid username or password, show error message
                messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def welcome(request):
    return render(request, 'welcome.html')

def logout_view(request):
    logout(request)
    return redirect('/login')

def image_render(request):
    uploaded_image = None
    if uploaded_image_id := request.GET.get('uploaded_image_id'):
        uploaded_image = uploaded_image.get(id=uploaded_image_id)

    return render(request, 'upload_image.html', {'uploaded_image': uploaded_image})

def display_skin_disease_image_by_id(request, image_id):
    # Filter SkinDiseaseImage by ID
    try:
        image = SkinDiseaseImage.objects.get(pk=image_id)
    except SkinDiseaseImage.DoesNotExist:
        # Handle the case where the image with the specified ID does not exist
        return render(request, 'image_not_found.html')

    # Pass the filtered image to the template for rendering
    return render(request, 'image_detail.html', {'image': image})


