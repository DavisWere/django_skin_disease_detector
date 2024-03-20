import requests

def get_geolocation(address):
    url = 'https://nominatim.openstreetmap.org/search'
    params = {
        'format': 'json',
        'q': address
    }
    response = requests.get(url, params=params)
    data = response.json()
    if data:
        # Assuming the first result is the most relevant one
        location = data[0]
        return float(location['lat']), float(location['lon'])
    else:
        print("Failed to get coordinates for the address.")
        return None, None

address = "Nairobi Hospital, Kenya"

latitude, longitude = get_geolocation(address)
if latitude is not None and longitude is not None:
    print("Latitude:", latitude)
    print("Longitude:", longitude)
else:
    print("Failed to get coordinates for the address.")

get_geolocation(address)

