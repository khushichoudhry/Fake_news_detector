import streamlit as st
import joblib

# Load the trained model pipeline
model = joblib.load("fake_news_model.pkl")

st.title("📰 Fake News Detector")
st.write("Enter a news article or headline below to check if it's likely Real or Fake.")

# Text input box for user
user_input = st.text_area("News Article Text:", height=150)

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter some text first.")
    else:
        # Make prediction using the pipeline
        prediction = model.predict([user_input])[0]

    # Map label (1 = Real, 0 = Fake)
    label = "Real News ✅" if prediction == 1 else "Fake News ❌"

    # Display result
    st.subheader(f"Prediction:{label}")
