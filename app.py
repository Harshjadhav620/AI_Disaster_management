import joblib

model = joblib.load("models/disaster_model.pkl")

print("Disaster Risk Pridiction System")
print("This sysstem predicts whether there is a HIGH or LOW disaster risk.")
print("-----------------------------------------------------------------------------\n")

while True:
    rainfall = float(input("Enter the Rainfall (mm): "))
    temperature = float(input("Enter temperature (c): "))
    soil_moisture = float(input("Enter Soil moisture (0 to 1): "))

    sample = [[rainfall,temperature,soil_moisture]]
    prediction = model.predict(sample)

    if prediction[0] == 1:
        print("High risk of disaster! Take precaution.\n")
    else:
        print("Low risk. Situation is safe.\n")

    again = input("Do you want to check again? (yes/no): ").strip().lower()
    if again != "yes" :
        print("\nThank you for using the system. Stay safe!")
        break     
    