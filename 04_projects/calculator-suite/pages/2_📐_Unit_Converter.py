import streamlit as st

st.set_page_config(page_title="Unit Converter", page_icon="📐", layout="centered")

st.sidebar.markdown("# ⚙️ Main Menu")
st.sidebar.markdown("---")

st.title("📐 Smart Unit Converter")
st.markdown("---")

category = st.selectbox("Select Conversion Category", ["Length", "Weight", "Temperature"])

if category == "Length":
    st.subheader("Length Converter")
    units = ["Meters", "Kilometers", "Miles", "Feet", "Inches"]
    from_unit = st.selectbox("From Unit", units, key="l1")
    to_unit = st.selectbox("To Unit", units, key="l2")
    val = st.number_input("Enter Value", min_value=0.0, value=1.0)
    
    to_meters = {"Meters": 1.0, "Kilometers": 1000.0, "Miles": 1609.34, "Feet": 0.3048, "Inches": 0.0254}
    val_in_meters = val * to_meters[from_unit]
    result = val_in_meters / to_meters[to_unit]
    st.success(f"Result: **{val} {from_unit} = {result:.4f} {to_unit}**")

elif category == "Weight":
    st.subheader("Weight Converter")
    units = ["Kilograms", "Grams", "Pounds", "Ounces"]
    from_unit = st.selectbox("From Unit", units, key="w1")
    to_unit = st.selectbox("To Unit", units, key="w2")
    val = st.number_input("Enter Value", min_value=0.0, value=1.0)
    
    to_kg = {"Kilograms": 1.0, "Grams": 0.001, "Pounds": 0.453592, "Ounces": 0.0283495}
    val_in_kg = val * to_kg[from_unit]
    result = val_in_kg / to_kg[to_unit]
    st.success(f"Result: **{val} {from_unit} = {result:.4f} {to_unit}**")

elif category == "Temperature":
    st.subheader("Temperature Converter")
    units = ["Celsius", "Fahrenheit", "Kelvin"]
    from_unit = st.selectbox("From Unit", units, key="t1")
    to_unit = st.selectbox("To Unit", units, key="t2")
    val = st.number_input("Enter Value", value=0.0)
    
    if from_unit == to_unit:
        result = val
    elif from_unit == "Celsius":
        result = (val * 9/5) + 32 if to_unit == "Fahrenheit" else val + 273.15
    elif from_unit == "Fahrenheit":
        result = (val - 32) * 5/9 if to_unit == "Celsius" else (val - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin":
        result = val - 273.15 if to_unit == "Celsius" else (val - 273.15) * 9/5 + 32
        
    st.success(f"Result: **{val}° {from_unit} = {result:.2f}° {to_unit}**")