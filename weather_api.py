import requests 
import pickle

with open("models/disaster_model.pkl","rb") as f:
    model = pickle.load(f)

API_KEY = "a5541cf683a2427d05784227305fb2d4"  
CITY = "Mumbai" 

URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
response = requests.get(URL)
data = response.json()

if response.status_code == 200:

    temperature = data["main"]["temp"]
    soil_moisture = 0.5
    rainfall = data.get("rain",{}).get("1h",0)

    print(f"City: {CITY}")
    print(f"Temperature: {temperature}c")
    print(f"Rianfall: {rainfall}mm")
    print(f"Soil moisture: {soil_moisture}")


    sample = [[rainfall,temperature,soil_moisture]]
    prediction = model.predict(sample)


    if prediction[0] == 1:
        print("High risk of disaster! Take precautions.")
    else:
        print("Low risk. Situation is safe.")
else:
    print("Error fetching weather data:", data)