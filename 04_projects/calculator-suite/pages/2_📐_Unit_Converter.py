import streamlit as st
from modules.converter_logic import convert_length, convert_weight, convert_temp
from modules.ui_components import add_footer

st.title("📐 Smart Unit Converter")
category = st.selectbox("Select Category", ["Length", "Weight", "Temperature"])

val_input = st.text_input("Enter Value", value="1.0")

if category == "Length":
    units = ["Meters", "Kilometers", "Miles", "Feet", "Inches"]
    from_u = st.selectbox("From", units)
    to_u = st.selectbox("To", units)
    if st.button("Convert"):
        res = convert_length(float(val_input), from_u, to_u)
        st.success(f"Result: {res:.4f} {to_u}")

elif category == "Weight":
    units = ["Kilograms", "Grams", "Pounds", "Ounces"]
    from_u = st.selectbox("From", units)
    to_u = st.selectbox("To", units)
    if st.button("Convert"):
        res = convert_weight(float(val_input), from_u, to_u)
        st.success(f"Result: {res:.4f} {to_u}")

elif category == "Temperature":
    units = ["Celsius", "Fahrenheit", "Kelvin"]
    from_u = st.selectbox("From", units)
    to_u = st.selectbox("To", units)
    if st.button("Convert"):
        res = convert_temp(float(val_input), from_u, to_u)
        st.success(f"Result: {res:.2f} {to_u}")

add_footer()

