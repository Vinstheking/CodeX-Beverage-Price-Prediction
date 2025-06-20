import streamlit as st
from prediction_helper import predict  # Ensure this is correctly linked to your prediction_helper.py

# Set the page configuration and title
st.set_page_config(page_title="CodeX Beverage: Price Prediction", page_icon="📊")
st.markdown(
    "<h1 style='text-align: center;'>CodeX Beverage: Price Prediction</h1>",
    unsafe_allow_html=True
)
st.markdown("\n")

import streamlit as st

# Set page layout to wide
st.set_page_config(layout="wide")

# Row 1
row1 = st.columns([2, 2, 2, 2])  # Adjust column widths
with row1[0]:
    age = st.number_input('Age', min_value=18, step=1, max_value=100, value=28)
with row1[1]:
    gender = st.selectbox('Gender', ['M', 'F'])
with row1[2]:
    zone = st.selectbox('Zone', ['Urban', 'Metro', 'Rural', 'Semi-Urban'])
with row1[3]:
    occupation = st.selectbox('Occupation', ['Working Professional', 'Student', 'Entrepreneur', 'Retired'])

# Row 2
row2 = st.columns([2, 2, 2, 2])
with row2[0]:
    income_levels = st.selectbox('Income Levels (Lahks)', ['<10L', '> 35L', '16L - 25L', 'Not Reported', '10L - 15L', '26L - 35L'])
with row2[1]:
    consume_frequency = st.selectbox('Consume Frequency(weekly)', ['3-4 times', '5-7 times', '0-2 times'])
with row2[2]:
    current_brand = st.selectbox('Current Brand', ['Newcomer', 'Established'])
with row2[3]:
    preferable_consumption_size = st.selectbox('Preferable Consumption Size', ['Medium (500 ml)', 'Large (1 L)', 'Small (250 ml)'])

# Row 3
row3 = st.columns([2, 2, 2, 2])
with row3[0]:
    awareness_of_other_brands = st.selectbox('Awareness of other Brands', ['0 to 1', '2 to 4', 'above 4'])
with row3[1]:
    reasons_for_choosing_brands = st.selectbox('Reasons for choosing brands', ['Price', 'Quality', 'Availability', 'Brand Reputation'])
with row3[2]:
    flavor_preference = st.selectbox('Flavor Preference', ['Traditional', 'Exotic'])
with row3[3]:
    purchase_channel = st.selectbox('Purchase Channel', ['Online', 'Retail Store'])

# Row 4
row4 = st.columns([2, 2, 2,2])  # Adjusted widths for fewer columns
with row4[0]:
    packaging_preference = st.selectbox('Packaging Preference', ['Simple', 'Premium', 'Eco-Friendly'])
with row4[1]:
    health_concerns = st.selectbox('Health concerns', ['Medium (Moderately health-conscious)', 'Low (Not very concerned)', 'High (Very health-conscious)'])
with row4[2]:
    typical_consumption_situations = st.selectbox('Typical consumption situations', ['Active (e.g., Sports, gym)', 'Social (e.g., Parties)', 'Casual (e.g., At home)'])


if st.button('Calculate Price Range'):

    price_range = predict(age,gender,zone,occupation,income_levels,consume_frequency,current_brand,preferable_consumption_size,
                          awareness_of_other_brands,reasons_for_choosing_brands,flavor_preference,purchase_channel,
                          packaging_preference,health_concerns,typical_consumption_situations)

    # Display the results
    st.write(f"Price Range: {price_range[0]} INR")



