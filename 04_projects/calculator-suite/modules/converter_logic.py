def convert_length(value, from_u, to_u):
    # Base: Meters
    factors = {"Meters": 1.0, "Kilometers": 1000.0, "Miles": 1609.34, "Feet": 0.3048, "Inches": 0.0254}
    meters = value * factors[from_u]
    return meters / factors[to_u]

def convert_weight(value, from_u, to_u):
    # Base: Kilograms
    factors = {"Kilograms": 1.0, "Grams": 0.001, "Pounds": 0.453592, "Ounces": 0.0283495}
    kgs = value * factors[from_u]
    return kgs / factors[to_u]

def convert_temp(value, from_u, to_u):
    if from_u == to_u: return value
    # Celsius to others
    if from_u == "Celsius":
        if to_u == "Fahrenheit": return (value * 9/5) + 32
        if to_u == "Kelvin": return value + 273.15
    # Fahrenheit to others
    if from_u == "Fahrenheit":
        c = (value - 32) * 5/9
        return c if to_u == "Celsius" else c + 273.15
    # Kelvin to others
    if from_u == "Kelvin":
        c = value - 273.15
        return c if to_u == "Celsius" else (c * 9/5) + 32