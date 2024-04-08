from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from .forms import SkinDiseaseImageForm, CustomUserRegistrationForm ,LoginForm
from django.contrib import messages
from .models import TensorflowResult, SkinDiseaseImage, Hospital, CustomUser, History
from django.contrib.auth.models import User
from .forms import LoginForm
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.utils.html import escape
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
import random
import pandas as pd
import openpyxl 
# from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference 
from openpyxl.styles import PatternFill
from openpyxl.drawing.colors import ColorChoice
from io import BytesIO
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from django.http import HttpResponse
import random
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

import requests
#from wkhtmltopdf.views import PDFTemplateResponse
# from weasyprint import HTML

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

from . import geolocation as GL
MAPBOX_API_KEY = 'pk.eyJ1IjoidmljdHJvbiIsImEiOiJjbHU5emVmcmgwY2dqMm5xazZqbTFlYTd1In0.-BzT0RVwGtYQ1B6c2x1YEQ'
MAPBOX_HOSPITALS_URL = 'https://api.mapbox.com/datasets/v1/mapbox/covid-19-testsites-us?access_token={api_key}'


def maps(request):
    return render(request, 'components/maps.html')


# Define the view function
def find_nearest_hospitals(request):
    try:
        # Obtain user's IP address
        user_ip = request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR', ''))

        # Use IP geolocation service to obtain user's location (latitude and longitude)
        ip_api_url = f'http://ip-api.com/json/{user_ip}'
        ip_response = requests.get(ip_api_url)
        ip_data = ip_response.json()

        # Extract latitude and longitude from the IP geolocation response
        if ip_data['status'] == 'success':
            latitude = ip_data['lat']
            longitude = ip_data['lon']
        else:
            # Use default coordinates for Nairobi if IP geolocation fails
            latitude = -1.286389
            longitude = 36.817223

        # Mapbox API endpoint for finding places (hospitals in this case)
        mapbox_api_key = 'YOUR_MAPBOX_API_KEY'
        url = f"https://api.mapbox.com/geocoding/v5/mapbox.places/hospital.json?proximity={longitude},{latitude}&access_token={MAPBOX_API_KEY}"

        # Make a GET request to the Mapbox API
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for any HTTP errors

        # Parse the JSON response
        data = response.json()

        # Check if the features list is empty
        if 'features' in data and data['features']:
            # Extract hospital information from the response
            hospitals = []
            for feature in data['features']:
                hospitals.append({
                    'name': feature['text'],
                    'address': ', '.join(feature['place_name'].split(',')[1:]),  # Extracting the address part from the full place name
                    'latitude': feature['geometry']['coordinates'][1],
                    'longitude': feature['geometry']['coordinates'][0],
                })
        else:
            # If no hospitals found, return an empty list
            hospitals = []

        # Calculate bounding box coordinates for Kenya
        kenya_bbox = [33.501601, -4.677098, 41.90625, 5.237941]  # [min_lon, min_lat, max_lon, max_lat]

        # Render the template with the list of hospitals and Kenya bounding box
        return render(request, 'components/hospital_list.html', {'hospitals': hospitals, 'kenya_bbox': kenya_bbox})

    except requests.exceptions.RequestException as e:
        # Handle request exceptions (e.g., connection errors, timeout)
        error_message = f"Error: {e}"
        return render(request, 'error.html', {'error_message': error_message})
def hospital_data(request):
    # Define hospital details
    
    hospitals = [
        {
            'name': 'Mp Shah',
            'website': 'https://mpshahhosp.org/',
            'contact': '+254 111 000600',
        },
        {
            'name': 'The Nairobi Hospital',
            'website': 'http://thenairobihosp.org/',
            'contact': '+254 20 2845000',
        },
        {
            'name': 'Mater Misericordiae Hospital',
            'website': 'http://www.materkenya.com/',
            'contact': '+254 20 6903000',
        },
        {
            'name': 'Avenue Hospital Nairobi',
            'website': 'http://www.avenuehealthcare.com/',
            'contact': '+254 711 060000',
        },
    ]

    # Shuffle the hospitals list to insert data at random
    random.shuffle(hospitals)

    # Insert data into the Hospital model
    for hospital_data in hospitals:
        Hospital.objects.create(
            name=hospital_data['name'],
            website=hospital_data['website'],
            contact=hospital_data['contact'],
        )

    # Get all hospitals from the database
    all_hospitals = Hospital.objects.all()

    # Render a template with the inserted hospital data for demonstration
    return render(request, 'upload_image.html', {'hospitals': all_hospitals})


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

    
@login_required
def insert_data_into_database(request, user):
 
    random_disease, random_accuracy = generate_data()
    
    # Print the random disease and accuracy to debug
    # print(" Disease:", random_disease)
    # print("Accuracy:", random_accuracy)

    # Create a TensorflowResult instance with the random disease and accuracy
    print(random_accuracy, 'random accuracied')
    result = TensorflowResult.objects.create(skin_diseases=random_disease, accuracy=random_accuracy, user=user)
    # print("Created TensorflowResult:", result)


def generate_excel_file(request):
    # Query the database to retrieve all TensorflowResult objects
    results = TensorflowResult.objects.all(),
    

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
    # pdf = HTML(string=data)

    # Create a table
    table = Table(data)

    # Style the table
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ])

    # Apply the table style
    table.setStyle(style)

    # Build the PDF document with the table
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


def upload_image( request):
    success_message = None  # Initialize success message variable
    error_message = None  # Initialize error message variable

    if request.method == 'POST':
        form = SkinDiseaseImageForm(request.POST, request.FILES)
        request.user
        test_user = request.user
        
        if form.is_valid():
            if request.FILES.get('image', False):  # Check if an image file is uploaded
                form.instance.user = request.user 
                form.instance.hospital = Hospital.objects.last()
                form.save()
                # success_message = ''
                
                hospital_data(request)
                print('hosi', hospital_data(request), '\n', '\n')
                user = request.user            
                insert_data_into_database(request, user)    

                history = History.objects.create(hospital=Hospital.objects.last(), 
                user=request.user,tensorflow_result=TensorflowResult.objects.last(), skin_disease_image= SkinDiseaseImage.objects.last() )

                messages.success(request, success_message)
                latest_result = TensorflowResult.objects.last()
                hospitals = Hospital.objects.order_by('-id')[:2]
               
                context = {'latest_result': latest_result}
                last_uploaded_image = SkinDiseaseImage.objects.last()
    
    # Check if any images exist in the database
                if last_uploaded_image is not None:
                    context = {'latest_result':latest_result,'image': last_uploaded_image,'user':user, 'hospitals':hospitals}
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
            return redirect('/login')  
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
                return redirect('/upload/')  # Redirect to the upload image page
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

@login_required
def display_data (request):
    user = request.user
    if user is not None:
        if user.is_superuser:
            diseases= TensorflowResult.objects.all()
            hospitals = Hospital.objects.all()
            users= CustomUser.objects.all()
            images = SkinDiseaseImage.objects.all()
            history = History.objects.all()
             
            values = []
            matched_images_and_users = []

            for hist in history:
                print('hist', hist, '\n')

            # for image in images:
            #     for user1 in users:
            #         for disease in diseases:
            #             if image.user == user1 and user1 == disease.user:
            #                 already_added = False
            #                 for item in matched_images_and_users:
            #                     if item['user'] == user1 and item['image'] == image.image and item['disease'] == disease:
            #                         already_added = True
            #                         break
            #                 if not already_added:
            #                     matched_images_and_users.append({'user': user1, 'image': image.image, 'disease': disease})
            #                     break   
            
            context = {'data': history}
            return render(request, 'admin.html', context)
        else:
            return redirect('/')
    else:
        return redirect('login')

       
    

# def generate_pdf_report(request):
#     user = request.user
#     if user is not None and user.is_superuser:
#         # Fetch data as per your existing view
#         diseases = TensorflowResult.objects.all()
#         hospitals = Hospital.objects.all()
#         users = CustomUser.objects.all()
#         images = SkinDiseaseImage.objects.all()

#         # Prepare data for PDF
#         data = []

#         for item in images:
#             data.append({
#                 'image': images[random.randint(0, len(images) - 1)].image.url,
#                 'user': users[random.randint(0, len(users) - 1)],
#                 'hospital': hospitals[random.randint(0, len(hospitals) - 1)],
#                 'diseases': diseases[random.randint(0, len(diseases) - 1)]
#             })

#         # Render HTML template using the data
#         template = get_template('pdf.html')
#         rendered_html = template.render({'data': data})

#         # Create PDF using reportlab and other libraries
#         # pdf_file = BytesIO()
#         # pisa_status = pisa.CreatePDF(
#         #     escape(rendered_html), dest=pdf_file)

#         # # Check if PDF generation was successful
#         # if not pisa_status.err:
#         #     # Set response headers for PDF download
#         #     response = HttpResponse(
#         #         pdf_file.getvalue(), content_type='application/pdf')
#         #     response['Content-Disposition'] = 'attachment; filename="report.pdf"'
#         #     return response


#         # Generate the PDF document
#         pdf = HTML(string=rendered_html)
#         pdf_document = pdf.write_pdf()

#         # Create a HTTP response with the PDF content
#         response = HttpResponse(content_type='application/pdf')
#         response['Content-Disposition'] = 'attachment; filename=output.pdf'
#         response.write(pdf_document)

#     # Handle unauthorized access or other conditions
#     return HttpResponse('Unauthorized or Error occurred.')

def generate_pdf_report(request):
    user = request.user
    if user is not None and user.is_superuser:
        obj_data = History.objects.all()

        # Create a BytesIO buffer to store the PDF content
        buffer = BytesIO()

        # Create a PDF canvas with landscape orientation
        doc = SimpleDocTemplate(buffer, pagesize=landscape(letter))
        elements = []

        # Define table data and styles
        table_data = [['Name', 'Patient Email','Hospital name','Diseases', 'accuracy']]
        for data in obj_data:
            hospital = data.hospital
            disease = data.tensorflow_result
            user = data.user
            table_data.append([user.first_name, user.email,  hospital.name, 
                               disease.skin_diseases, disease.accuracy])

        # Create the table
        table = Table(table_data, colWidths=[50, 150, 150, 200, 50])
        table_style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), '#A9A9A9'),
                                  ('TEXTCOLOR', (0, 0), (-1, 0), '#FFFFFF'),
                                  ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                  ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                                  ('INNERGRID', (0, 0), (-1, -1), 0.25, '#000000'),
                                  ('BOX', (0, 0), (-1, -1), 0.25, '#000000'),
                                  ('WORDWRAP', (0, 0), (-1, -1))]) 
        table.setStyle(table_style)
        elements.append(table)

        # Build the PDF document
        doc.build(elements)

        # Get the PDF content from the BytesIO buffer
        pdf_content = buffer.getvalue()
        buffer.close()

        # Create an HttpResponse object with the PDF content
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="report.pdf"'
        response.write(pdf_content)

        return response
    else:
        return HttpResponse("Unauthorized", status=401)