from django.db import models
from django.contrib.auth.models import AbstractUser
import os
from datetime import datetime
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.validators import RegexValidator
from django.utils import timezone

phone_validator = RegexValidator(r"^\d{9,10}$", "Enter a valid phone number.")

phone_code_validator = RegexValidator(r"^\+\d{1,3}$")

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    location = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return self.username

class SkinDiseaseImage(models.Model):
    image = models.ImageField(upload_to='skin_disease_images/')

class TensorflowResult(models.Model):
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

    accuracy = models.CharField(max_length= 4, blank=False, null= False)
    skin_diseases = models.CharField(max_length= 250, blank= True, null= True, choices= DISEASE_CHOICES)

    def __str__(self):
        return f"Disease: {self.skin_diseases}, Accuracy: {self.accuracy}"

class Hospital(models.Model):
    name =  models.CharField(max_length=200, blank =  False, null = False)
    website = models.CharField(max_length=500, blank= False, null=False)
    contact = models.CharField(max_length=40, blank=True, null= True)

    def __str__(self):
        return f"Hospitals:  {self.name}, {self.contact}  ,{self.website}"