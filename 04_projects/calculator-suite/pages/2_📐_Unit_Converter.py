import streamlit as st

st.title("📐 Smart Unit Converter")
st.markdown("---")

category = st.selectbox("Select Conversion Category", ["Length", "Weight", "Temperature"])

if category == "Length":
    units = ["Meters", "Kilometers", "Miles", "Feet", "Inches"]
    from_unit = st.selectbox("From Unit", units)
    to_unit = st.selectbox("To Unit", units)
    val_input = st.text_input("Enter Value", value="1.0")
    
    if val_input:
        try:
            val = float(val_input)
            to_meters = {"Meters": 1.0, "Kilometers": 1000.0, "Miles": 1609.34, "Feet": 0.3048, "Inches": 0.0254}
            result = (val * to_meters[from_unit]) / to_meters[to_unit]
            st.success(f"Result: **{val} {from_unit} = {result:.4f} {to_unit}**")
        except ValueError:
            st.warning("Enter a valid number")

elif category == "Weight":
    units = ["Kilograms", "Grams", "Pounds", "Ounces"]
    from_unit = st.selectbox("From Unit", units)
    to_unit = st.selectbox("To Unit", units)
    val_input = st.text_input("Enter Value", value="1.0")
    
    if val_input:
        try:
            val = float(val_input)
            to_kg = {"Kilograms": 1.0, "Grams": 0.001, "Pounds": 0.453592, "Ounces": 0.0283495}
            result = (val * to_kg[from_unit]) / to_kg[to_unit]
            st.success(f"Result: **{val} {from_unit} = {result:.4f} {to_unit}**")
        except ValueError:
            st.warning("Enter a valid number")

elif category == "Temperature":
    units = ["Celsius", "Fahrenheit", "Kelvin"]
    from_unit = st.selectbox("From Unit", units)
    to_unit = st.selectbox("To Unit", units)
    val_input = st.text_input("Enter Value", value="0.0")
    
    if val_input:
        try:
            val = float(val_input)
            if from_unit == to_unit: result = val
            elif from_unit == "Celsius": result = (val * 9/5) + 32 if to_unit == "Fahrenheit" else val + 273.15
            elif from_unit == "Fahrenheit": result = (val - 32) * 5/9 if to_unit == "Celsius" else (val - 32) * 5/9 + 273.15
            elif from_unit == "Kelvin": result = val - 273.15 if to_unit == "Celsius" else (val - 273.15) * 9/5 + 32
            st.success(f"Result: **{val}° {from_unit} = {result:.2f}° {to_unit}**")
        except ValueError:
            st.warning("Enter a valid number")