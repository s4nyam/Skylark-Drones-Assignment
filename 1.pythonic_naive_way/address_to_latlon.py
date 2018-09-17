from geopy.geocoders import Nominatim
userInput = raw_input("Enter Your Location:  ")
finalloc = str(userInput)
geolocator = Nominatim(user_agent="skylarkInc")

location = geolocator.geocode(finalloc)
print("Your Longitude and Latitide are respectively:")  
print(location.longitude,location.latitude)