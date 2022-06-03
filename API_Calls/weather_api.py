import urllib.request as url
import json
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="MyApp")

key = "83e01e3dce5d28839bb5a177cb51af12"
# lat = 28.7041
# lon = 77.1025
city = input("Enter location : ")
location = geolocator.geocode(city)
lat = location.latitude
lon = location.longitude
path = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}"
response = url.urlopen(path)
data = json.load(response)
temp = data['main']['temp'] - 273.5
print("Current Temperature in :",city,"is",temp)