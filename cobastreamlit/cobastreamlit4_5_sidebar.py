import streamlit as st
import time
#docs st.sidebar()

#EXAMPLE 1 :
#st.sidebar.header('Huawei apps store：')
#st.sidebar.subheader('1.please chose which app you want to operate')

#EXAMPLE 2 :
# add_selectbox = st.sidebar.selectbox(
#     "How would you like to be contacted?",
#     ("Email", "Home phone", "Mobile phone")
# )

# # Using "with" notation
# with st.sidebar:
#     add_radio = st.radio(
#         "Choose a shipping method",
#         ("Standard (5-15 days)", "Express (2-5 days)")
#     )

#EXAMPLE 3 :
with st.sidebar:
    with st.echo():
        st.write("This code will be printed to the sidebar.")

    with st.spinner("Loading..."):
        time.sleep(5)
    st.success("Done!")
