import streamlit as st
import pandas as pd
import joblib

# Load trained pipeline
model = joblib.load('model.pkl')

st.title("House Price Prediction")

# Numerical Inputs
area = st.number_input("Area")
bedrooms = st.number_input("Bedrooms")
bathrooms = st.number_input("Bathrooms")
stories = st.number_input("Stories")
parking = st.number_input("Parking")

# Categorical Inputs
mainroad = st.selectbox("Main Road",['yes','no'])
guestroom = st.selectbox("Guest Room",['yes','no'])
basement = st.selectbox("Basement",['yes','no'])
hotwaterheating = st.selectbox("Hot Water Heating",['yes','no'])
airconditioning = st.selectbox("Air Conditioning",['yes','no'])
prefarea = st.selectbox("Preferred Area",['yes','no'])

furnishingstatus = st.selectbox(
    "Furnishing Status",
    ['furnished','semi-furnished','unfurnished']
)

# Prediction
if st.button("Predict Price"):

    sample = pd.DataFrame({
        'area':[area],
        'bedrooms':[bedrooms],
        'bathrooms':[bathrooms],
        'stories':[stories],
        'parking':[parking],
        'mainroad':[mainroad],
        'guestroom':[guestroom],
        'basement':[basement],
        'hotwaterheating':[hotwaterheating],
        'airconditioning':[airconditioning],
        'prefarea':[prefarea],
        'furnishingstatus':[furnishingstatus]
    })

    prediction = model.predict(sample)

    st.success(f"Predicted Price: ₹ {prediction[0]:,.2f}")