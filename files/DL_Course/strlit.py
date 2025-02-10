import streamlit as st
import pandas as pd
import numpy as np

#title of the app
st.title("Streamlit App")

#display a text
st.write("This is st.write")

#create a simple dataframe
df = pd.DataFrame({
    'column1' : [1,2,3],
    'column2' : [4,5,6]
})

#display the dataframe:
st.write('Here is a dataframe')
st.write(df)

#create a linechart
chart_data = pd.DataFrame(np.random.randn(20,3),columns=['a','b','c'])
st.line_chart(chart_data)
