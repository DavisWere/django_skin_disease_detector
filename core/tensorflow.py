import random
Skin_diseases = [
    "Acne",
    "Eczema (Dermatitis)",
    "Psoriasis",
    "Rosacea",
    "Dermatitis Herpetiformis",
    "Skin Cancer",
    "Hives (Urticaria)",
    "Vitiligo",
    "Fungal Infections",
    "Scabies",
    "Atopic Dermatitis",
    "Contact Dermatitis",
    "Seborrheic Dermatitis",
    "Actinic Keratosis",
    "Basal Cell Carcinoma",
    "Squamous Cell Carcinoma",
    "Melanoma",
    "Keratosis Pilaris",
    "Lichen Planus",
    "Pityriasis Rosea",
    "Tinea Versicolor",
    "Impetigo",
    "Cellulitis",
    "Molluscum Contagiosum",
    "Warts",
    "Hidradenitis Suppurativa",
    "Ichthyosis",
    "Folliculitis",
    "Perioral Dermatitis",
    "Dyshidrotic Eczema",
    "Granuloma Annulare",
    "Lupus",
    "Scleroderma",
    "Epidermolysis Bullosa",
    "Prurigo Nodularis",
    "Pemphigus",
    "Pemphigoid",
    "Morbilliform Drug Eruption",
    "Stevens-Johnson Syndrome",
    "Toxic Epidermal Necrolysis",
    "Erythema Multiforme",
    "Cutaneous T-cell Lymphoma",
    "Kaposi's Sarcoma",
    "Pyoderma Gangrenosum",
    "Eosinophilic Pustular Folliculitis",
    "Necrobiosis Lipoidica",
    "Sweet's Syndrome",
    "Lichen Sclerosus",
    "Pruritus",
    "Xerosis",
    "Onychomycosis",
    "Pilonidal Cyst",
    "Lipoma",
    "Sebaceous Cyst",
    "Keloids",
    "Angiomas",
    "Dermatofibroma",
    "Chronic Hives",
    "Erythrasma",
    "Fordyce Spots",
    "Lichen Simplex Chronicus",
    "Miliaria (Heat Rash)",
    "Panniculitis",
    "Pyogenic Granuloma",
    "Tinea Barbae",
    "Tinea Capitis",
    "Tinea Corporis",
    "Tinea Cruris",
    "Tinea Pedis",
    "Tinea Unguium",
    "Verrucas",
    "Dermatomyositis",
    "Erythema Infectiosum (Fifth Disease)",
    "Keratosis Pilaris Rubra",
    "Pediculosis",
    "Pseudofolliculitis Barbae",
    "Seborrheic Keratosis",
    "Solar Lentigo",
    "Viral Exanthem"
]


skin_diseases = [
    "Acne", "Eczema (Dermatitis)", "Psoriasis", "Rosacea", "Dermatitis Herpetiformis",
    "Skin Cancer", "Hives (Urticaria)", "Vitiligo", "Fungal Infections", "Scabies",
    "Atopic Dermatitis", "Contact Dermatitis", "Seborrheic Dermatitis", "Actinic Keratosis",
    "Basal Cell Carcinoma", "Squamous Cell Carcinoma", "Melanoma", "Keratosis Pilaris",
    "Lichen Planus", "Pityriasis Rosea", "Tinea Versicolor", "Impetigo", "Cellulitis",
    "Molluscum Contagiosum", "Warts", "Hidradenitis Suppurativa", "Ichthyosis", "Folliculitis",
    "Perioral Dermatitis", "Dyshidrotic Eczema", "Granuloma Annulare", "Lupus", "Scleroderma",
    "Epidermolysis Bullosa", "Prurigo Nodularis", "Pemphigus", "Pemphigoid", "Morbilliform Drug Eruption",
    "Stevens-Johnson Syndrome", "Toxic Epidermal Necrolysis", "Erythema Multiforme",
    "Cutaneous T-cell Lymphoma", "Kaposi's Sarcoma", "Pyoderma Gangrenosum", "Eosinophilic Pustular Folliculitis",
    "Necrobiosis Lipoidica", "Sweet's Syndrome", "Lichen Sclerosus", "Pruritus", "Xerosis", "Onychomycosis",
    "Pilonidal Cyst", "Lipoma", "Sebaceous Cyst", "Keloids", "Angiomas", "Dermatofibroma"
]


random_index = random.randint(0, len(skin_diseases) - 1)
pass

print(skin_diseases[random_index])


accuracy = []

for i in range(10, 97, 3):
    percentage_string = str(i) + '%'
    accuracy.append(percentage_string)

# Append random accuracy values
random_index = random.randint(0, len(accuracy) - 1)
pass  # Generate a random index
# print(accuracy[random_index])