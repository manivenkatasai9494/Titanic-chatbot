from fastapi import FastAPI
import pandas as pd
import seaborn as sns

app = FastAPI()

# Load Titanic dataset from seaborn
df = sns.load_dataset('titanic')

@app.get("/")
def home():
    return {"message": "Titanic Chatbot API is running!"}

@app.get("/total_passengers")
def total_passengers():
    return {"total_passengers": len(df)}

@app.get("/male_percentage")
def male_percentage():
    male_count = df[df["sex"] == "male"].shape[0]
    percentage = (male_count / len(df)) * 100
    return {"male_percentage": percentage}

@app.get("/average_fare")
def average_fare():
    return {"average_fare": df["fare"].mean()}

@app.get("/embarked_counts")
def embarked_counts():
    return df["embark_town"].value_counts().to_dict()
