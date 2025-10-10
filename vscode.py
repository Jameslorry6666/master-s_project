
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import streamlit as st



# Set page config
st.set_page_config(page_title="df_drop.csv Analysis", layout="wide")
st.title("📊 Analyzing: Demential using MRI dataset")
st.write("**Python file:** vscode.py | **Data file:** df_drop.csv")

st.info("This application builds machine learning models")

with st.expander("Data"):
 st.write("**Raw data**")
    
 df = pd.read_csv("df_drop.csv")
 df