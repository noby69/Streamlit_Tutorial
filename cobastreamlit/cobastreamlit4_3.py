import streamlit as st
import time

st.balloons()
st.progress(20)
with st.spinner('Wait for it...'):
    time.sleep(5)
    #st.success('Done!')

#menghilangkan burger dan made with streamlit
hide_streamlit_style = """
 <style>
  #MainMenu {visibility: hidden;}
  footer {visibility: hidden;}
 </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)    