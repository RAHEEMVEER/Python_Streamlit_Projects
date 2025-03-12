import streamlit as st
import string
import random

def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    return password

st.title("Password Generator")

length = st.slider("Length of password", 4, 30, 8)
use_digits = st.checkbox("Include digits")
use_special = st.checkbox("Include special characters")

if st.button("Generate password"):
    password = generate_password(length, use_digits, use_special)
    st.write(f"Generated Password: {password}")