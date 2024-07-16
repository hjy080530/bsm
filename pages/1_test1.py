import streamlit as st
st.session_state.jum = 0 
st.title("printf를 스기위해 써야하는 헤더파일은?")
pro1 = st.checkbox("stdio.h")
pro2 = st.checkbox("std2io.h")
pro3 = st.checkbox("stdi3o.h")
pro4 = st.checkbox("stdio1.h")
pro5 = st.checkbox("stdiro.h")
if st.button("확인"):
   if pro1:
     st.session_state.jum=st.session_state.jum+50
