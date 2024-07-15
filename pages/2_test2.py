import streamlit as st

title=st.text_input("Hello World를 출력하시오")
if st.button("확인"):
  if title=='printf("Hello World")':
    st.session_state.jum=st.session_state.jum+50
