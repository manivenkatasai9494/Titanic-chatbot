import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("🚢 Titanic Chatbot")

BASE_URL = "http://127.0.0.1:8000"

# User Input
question = st.text_input("Ask me about the Titanic dataset!")

if st.button("Submit"):
    if "percentage of passengers were male" in question:
        response = requests.get(f"{BASE_URL}/male_percentage").json()
        st.write(f"🚹 Male passengers: {response['male_percentage']:.2f}%")

    elif "average ticket fare" in question:
        response = requests.get(f"{BASE_URL}/average_fare").json()
        st.write(f"💰 Average ticket fare: ${response['average_fare']:.2f}")

    elif "passengers embarked from each port" in question:
        response = requests.get(f"{BASE_URL}/embarked_counts").json()
        st.write("🚢 Number of passengers from each port:")
        st.write(pd.DataFrame(response.items(), columns=["Port", "Count"]))

    elif "histogram of passenger ages" in question:
        df = sns.load_dataset('titanic')
        plt.figure(figsize=(8, 4))
        sns.histplot(df["age"].dropna(), bins=20, kde=True)
        st.pyplot(plt)

    else:
        st.write("❓ I don't understand that question yet. Try asking about male percentage, fare, embarkation, or age distribution.")
