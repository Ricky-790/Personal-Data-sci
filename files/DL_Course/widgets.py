import streamlit as st
import pandas as pd

st.title("Streamlit Widgets")

st.title("ST text input widget")

name = st.text_input("Enter your name")
if name:
    st.write("Hello", name)

age = st.slider('Select age', 0, 100, 25) #initial, final and default value
st.write("Your age is", age)

options = ["Python", "Java", "C++", "C#"]
choice = st.selectbox("Select a programming language", options)
st.write("You selected", choice)

uploaded_file = st.file_uploader("Upload a csv file", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)