import streamlit as st 

st.title("Power Calculator")
st.write("Enter a number to calculate its power till that number")

n = st.number_input("Ente a integer", value=1, step=1)

l= []
for i in range(n):
    l.append(n ** i)
    
st.write(l)
