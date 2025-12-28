import streamlit as st
import joblib

# Load saved model and vectorizer
model = joblib.load("fake_news_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

st.title("📰 Fake News Detection System")
st.write("Enter a news article below to check whether it is Fake or Real.")

news_text = st.text_area("News Text", height=200)

if st.button("Check News"):
    if news_text.strip() == "":
        st.warning("Please enter some text")
    else:
        text_vector = vectorizer.transform([news_text])
        prediction = model.predict(text_vector)
        probability = model.predict_proba(text_vector)

        confidence = max(probability[0]) * 100

        if prediction[0] == 1:
            st.success(f"✅ This news is REAL \n\nConfidence: {confidence:.2f}%")
        else:
            st.error(f"❌ This news is FAKE \n\nConfidence: {confidence:.2f}%")

