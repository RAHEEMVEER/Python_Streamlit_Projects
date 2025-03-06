import streamlit as st

def unit_converter(val, from_unit, to_unit):
    conversion = {
        "meter_to_kilometer": 0.001,
        "kilometer_to_meter": 1000,
        "gram_to_kilogram": 0.001,
        "kilogram_to_gram": 1000,
    }

    key = f"{from_unit}_to_{to_unit}"
    if (key in conversion):
        convert = conversion.get(key)
        return val * convert
    else:
        return "Conversion not available"

st.title("Unit Converter App") 

user_value = st.number_input("Enter the value", min_value = 1, step = 1)
unit_from = st.selectbox("Convert From", ["meter", "kilometer", "gram", "kilogram"])
unit_to = st.selectbox("Convert To", ["meter", "kilometer", "gram", "kilogram"])

if st.button("Convert"):
    result = unit_converter(user_value, unit_from, unit_to)
    st.write(f"Converted Value: {int(result)} {unit_to}")