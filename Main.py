import streamlit as st
import firebase_admin
from firebase_admin import credentials

from firebase_admin import db

# Get a database reference to our posts
ref = db.reference('key', url='https://bssm-c7af4-default-rtdb.firebaseio.com/')

st.write("학번")
title=st.text_input("")
st.write("이름")
titi1=st.text_input("",key="hh")
if st.button("Save"):
    st.session_state.hh=titi1
jum=0 
ref.update({title:titi1})