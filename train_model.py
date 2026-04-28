import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load data
df = pd.read_csv("crop_data.csv")

# Features
X = df[["temperature", "humidity", "rainfall"]]
y = df["label"]

# Model
model = RandomForestClassifier()
model.fit(X, y)

# Save
pickle.dump(model, open("model.pkl", "wb"))

print("Model trained successfully ✅")