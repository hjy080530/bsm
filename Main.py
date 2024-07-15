import streamlit as st
title=st.text_input("")
if st.button("Save"):
    st.session_state.student=title
jum=0 