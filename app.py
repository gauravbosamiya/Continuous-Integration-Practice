import streamlit as st 

st.title("Power Calculator")
st.write("Enter a number to calculate square, cub, and fifth power")

n = st.number_input("Ente a integer", value=1, step=1)

square = n**2
cube = n**3
fifth = n**5

st.write(f"square of {n} is", square)
st.write(f"cube of {n} is", cube)
st.write(f"fifth power of {n} is", fifth)
