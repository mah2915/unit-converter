import streamlit as st

# Declaring conversion factors
length_units = {"Meters" : 1,"Kilometers":0.001, "Miles":0.000621371,"foots":3.28084, "Centimeters":100.0000032, "Millimeters":1000.000032, "Micrometers":1000000.032,"Inch":39.3701}
mass_units = {"Grams" : 1,"Kilograms":0.001, "milligram":1000,"pounds":0.00220462, "ounces":0.035274}

# Streamlit ui
st.title("🔄 Unit Converter")

conversion_type= st.selectbox("Choose conversion type",["length","mass"])

if conversion_type == "length":
    units = length_units
else:
    units = mass_units

from_unit = st.selectbox("From",units.keys())
to_unit = st.selectbox("To",units.keys())

value = st.number_input("Enter Value",min_value=0.00,format="%.4f")

if st.button("Convert"):
    result = (value*(units[to_unit]/units[from_unit]))
    st.success(f"Converted value: {result:.4f}{to_unit}")