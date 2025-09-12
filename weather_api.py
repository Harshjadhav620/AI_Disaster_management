import requests
import joblib

# Load the trained model
model = joblib.load("models/disaster_model.pkl")

API_KEY = "a5541cf683a2427d05784227305fb2d4"   # replace with your OpenWeatherMap key
CITY = "Lonavala"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

try:
    response = requests.get(URL)
    data = response.json()

    if response.status_code == 200:
        temperature = data["main"]["temp"]           # in Celsius
        rainfall = data.get("rain", {}).get("1h", 0) # rain in last 1 hour, default = 0
        soil_moisture = 0.5  # placeholder (since API does not provide directly)

        print(f"City: {CITY}")
        print(f"Temperature: {temperature}°C")
        print(f"Rainfall: {rainfall} mm")
        print(f"Soil moisture: {soil_moisture}")

        # Prepare input for prediction
        sample = [[rainfall, temperature, soil_moisture]]
        prediction = model.predict(sample)

        if prediction[0] == 1:
            print("⚠ High risk of disaster! Take precautions.\n")
        else:
            print("✅ Low risk. Situation is safe.\n")

    else:
        print("Error fetching weather data:", data)

except Exception as e:
    print("Error:", e)
