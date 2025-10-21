
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import streamlit as st



# Set page config
st.set_page_config(page_title="df_drop.csv Analysis", layout="wide")
st.title("📊 Analyzing: Demential using MRI dataset")
st.write("**Python file:** vscode.py | **Data file:** df_drop.csv|Developed by James")

st.info("This application builds machine learning models")

with st.expander("Data"):
 st.write("**Raw data**")
 df = pd.read_csv("df_drop.csv")
 df


#data cleaning with st.expander("Data"):
with st.expander("Data_Preprocessing"):
  st.write("**Data_Cleaning**")
  st.write(df.isnull().sum().sum())

#data shape

  st.write("**Data shape**")
  st.write(df.shape)



  st.write("**Data describe**")
  st.write(df.describe())

  # preparing data for machine learning training

  st.write("**Data**")
  st.write("**X**")
  X =df
  X


  

  st.write(X['Hand'].value_counts())
  st.write(X['M/F'].value_counts())
  st.write(X['Group'].value_counts())


  #mapping 
  st.dataframe(X['M/F'])

  dictionary={'M':0, 'F':1}
  X['GENDER']= X['M/F'].map(dictionary)
  st.write( X['GENDER']) #'M':0, 'F':1

  




  dictionary = {'Demented':1, 'Nondemented':0,'Converted':1 }
  X['Targets']= X['Group'].map(dictionary)
  
  st.write("**new_df**")
  new_df = X[['Visit', 'MR Delay','Age','EDUC','SES','MMSE','eTIV','nWBV','ASF','CDR','GENDER','Targets']]
  new_df 



with st.sidebar:
    st.header("Features Input")
    
    # Visit - Selectbox with numbers 1-5
    visit = st.selectbox(
        'Visit',
        options=[1, 2, 3, 4, 5],
        index=0  # Default to first visit
    )
    
    # MR Delay - Number input (assuming continuous)
    mr_delay = st.number_input(
        'MR Delay',
        min_value=0.0,
        max_value=1000.0,
        value=0.0,  # Default value
        step=0.1
    )
    
    # Age - Number input
    age = st.number_input(
        'Age',
        min_value=0,
        max_value=120,
        value=30,  # Default age
        step=1
    )
    
    # EDUC - Education (number input)
    educ = st.number_input(
        'EDUC',
        min_value=0,
        max_value=25,  # Assuming years of education
        value=12,  # Default high school
        step=1
    )
    
    # SES - Socioeconomic Status (selectbox or slider)
    ses = st.selectbox(
        'SES',
        options=[1, 2, 3, 4, 5],  # Common SES scale 1-5
        format_func=lambda x: f"Level {x}"
    )
    
    # MMSE - Mini-Mental State Examination (slider)
    mmse = st.slider(
        'MMSE',
        min_value=0,
        max_value=30,  # MMSE range
        value=28,  # Default normal score
        step=1
    )
    
    # eTIV - Estimated Total Intracranial Volume (number input)
    etiv = st.number_input(
        'eTIV',
        min_value=0.0,
        max_value=2500.0,  # Typical range in cm³
        value=1500.0,
        step=1.0
    )
    
    # nWBV - Normalized Whole Brain Volume (slider)
    nwbv = st.slider(
        'nWBV',
        min_value=0.0,
        max_value=1.0,  # Normalized range
        value=0.75,  # Default value
        step=0.01
    )
    
    # ASF - Atlas Scaling Factor (number input)
    asf = st.number_input(
        'ASF',
        min_value=0.5,
        max_value=2.0,  # Typical range
        value=1.0,  # Default
        step=0.01
    )
    
    # CDR - Clinical Dementia Rating (selectbox)
    cdr = st.selectbox(
        'CDR',
        options=[0.0, 0.5, 1.0, 2.0, 3.0],  # Standard CDR levels
        format_func=lambda x: f"CDR {x}"
    )
    
    # GENDER - Selectbox
    gender = st.selectbox(
        'GENDER',
        options=[0, 1],
        format_func=lambda x: "Male" if x == 0 else "Female"
    )
    
    
  


with st.expander("Features_Targets"):

  X = new_df.drop(['MR Delay','Targets'], axis=1)
  st.write("**X**")
  X


  st.write("**y**")
  y = new_df['Targets']
  y







