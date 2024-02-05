# pip install streamlit streamlit-player
import streamlit as st

st.write("""
        # My first app
        Hello *world!*
        """)
#st_player("http://192.168.68.102:8000/stream.mjpg")
st.video("http://192.168.68.102:8000/stream.mjpg", format="video/mjpg")
