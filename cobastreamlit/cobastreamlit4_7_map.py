import pandas as pd
import numpy as np
import streamlit as st

df=pd.DataFrame(np.random.randn(500, 2) / [50, 50] + [-6.23, 106.93],columns=['lat', 'lon'])
st.map(df)