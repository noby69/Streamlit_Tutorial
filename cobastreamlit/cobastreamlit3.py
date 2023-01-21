import streamlit as st

st.image("unsada_logo.jpg")
st.audio("my_audio.mp3")
st.video("my_video.mp4")

#menghilangkan burger dan made with streamlit
hide_streamlit_style = """
 <style>
  #MainMenu {visibility: hidden;}
  footer {visibility: hidden;}
 </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)