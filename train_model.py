import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

df = pd.read_csv("data/disaster_data.csv")
print("... Dataset loaded sucessfully!")
print(df.head())

x = df[["rainfall","temperature","soil_moisture"]]
y = df['disaster']
print("\n... features and target selected!")
print(x.head())
print(y.head())

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

model = RandomForestClassifier(random_state=42)
model.fit(x_train,y_train)

y_pred = model.predict(x_test)
accuracy = accuracy_score(y_test,y_pred)
print(f"... Model trained! Accuracy: {accuracy:.2f}")

joblib.dump(model,"models/disaster_model.pkl")
print("... Model saved in models/disaster_model.pkl")


