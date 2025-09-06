import joblib

model = joblib.load("models/disaster_model.pkl")
print("... Model loaded successfully!")

rainfall = float(input("Enter the rainfall (mm):"))
temperature = float(input("Enter the temperature (°C):"))
soil_moisture = float(input("Enter soil moisture (0 to 1):"))

sample = [[rainfall,temperature,soil_moisture]]

prediction = model.predict(sample)

if prediction[0]==1:
    print("... Disaster Risk: HIGH (1)")
else:
    print("... Disaster Risk: LOW (0)")