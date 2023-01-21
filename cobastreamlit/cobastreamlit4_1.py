import streamlit as st

st.checkbox('yes')
st.button('Click')
st.radio('Pick your gender',['Male','Female'])
st.selectbox('Pick your gender',['Male','Female'])
st.multiselect('choose a planet',['Jupiter', 'Mars', 'Neptune'])
st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
st.slider('Pick a number', 0,50)

#menghilangkan burger dan made with streamlit
hide_streamlit_style = """
 <style>
  #MainMenu {visibility: hidden;}
  footer {visibility: hidden;}
 </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)