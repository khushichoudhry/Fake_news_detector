import streamlit as st
import pickle

# Load trained model
with open("fake_news_model.pkl", "rb") as file:
    model = pickle.load(file)

# Page settings
st.set_page_config(
    page_title="Fake News Detection",
    page_icon="📰",
    layout="centered"
)

st.title("📰 Fake News Detection System")
st.write("Check whether news is Fake or Real.")

# News input
news = st.text_area(
    "Enter News Here:",
    placeholder="Type or paste your news..."
)

# Prediction button
if st.button("Check News"):

    if news.strip():

        prediction = model.predict([news])[0]

        if prediction == 0:
            st.error("⚠️ This News is FAKE!")

        elif prediction == 1:
            st.success("✅ This News is REAL!")

        else:
            st.warning("Unknown Prediction")

    else:
        st.warning("Please enter news first.")