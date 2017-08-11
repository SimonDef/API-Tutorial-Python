import requests
import json
import urllib

def get_location():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    current_loc = response.json()
    return current_loc

def get_pass(location):
    response = requests.get("http://api.open-notify.org/iss-pass.json", params=location)
    data = response.json()
    return data

def get_astros():
    response = requests.get("http://api.open-notify.org/astros.json")
    data = response.json()
    return data

def find_location_address(lat, lng):
    maps_key = 'AIzaSyCAdWzytQ2jzCCisRqLdGT2omCyMYPscyA'
    geoloc_base_url = 'https://maps.googleapis.com/maps/api/geocode/json'

    # This joins the parts of the URL together into one string.
    url = geoloc_base_url + '?' + urllib.parse.urlencode({
        'latlng': "%s,%s" % (lat, lng),
        'key': maps_key,
    })
    response = requests.get(url)
    data = response.json()
    return data

hongkong = {"lat": 22.25, "lon": 114.1667}
#print(get_pass(hongkong))


country_list=[]
current_location = get_location()
current_location_address = find_location_address(current_location['iss_position']['latitude'],current_location['iss_position']['longitude'])

if current_location_address['status']=='ZERO_RESULTS':
    print("i dont know, probably in the sea")
else:
    for address in range (len(current_location_address['results'])):
        for item in range(len(current_location_address['results'][address]['address_components'])):
            if "country" in current_location_address['results'][address]['address_components'][item]['types']:
                country=current_location_address['results'][address]['address_components'][item]['long_name']
                if country not in country_list:
                    country_list.append(country)
print(country_list)