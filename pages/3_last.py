import streamlit as st
import firebase_admin
from firebase_admin import credentials

# Get a database reference to our posts
ref = db.reference('key', url='https://bssm-c7af4-default-rtdb.firebaseio.com/')

st.title("총점~",str(st.session_state.jum))
print(ref.get())