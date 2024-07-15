import streamlit as st
st.title("dsc")
st.title('_Streamlit_is :blue[cool] :sunglassese :trophy')
st.code('print("he")', language='phthon')
st.code('#include<stdio.h>',language='C')


st.caption('This is a string that explains something above.')
st.caption('A caption with _italics_ :blue[colors] and emojis :sunglasses:')

st.button("Reset", type="primary")

if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")