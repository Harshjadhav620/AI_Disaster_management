import pickle 

with open ("models/disaster_model.pkl","rb") as f:
    model = pickle.load(f)

print ("Disaster Risk Prediction System")
print ("This system predicts whether there is a HIGH or LOW disaster risk.")
print ("-------------------------------------------------------------------\n")

while True:

    rainfall = float(input("Enter the Rainfall (mm): "))
    temperature = float(input("Enter temperature (c):"))
    soil_moisture= float(input("Enter Soil moisture (0 to 1):"))

    sample = [[rainfall,temperature,soil_moisture]]

    prediction = model.predict(sample)

    if prediction[0] == 1:
            print ("High risk of disater! Take precuations.\n")
    else:
            print("Low risk. Situation is safe.\n")

    again = input("Do you want to cheak again? (yes/no): ").strip().lower()
    if again != "yes":
            print("\n Thank you for using the system. Stay safe!")
            break
    