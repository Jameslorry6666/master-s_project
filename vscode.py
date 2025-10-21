
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
  st.header("Features_Input")
  #visit= st.selectbox('Visit',1,2,3,4,5)
"Visit', 'MR Delay','Age','EDUC','SES','MMSE','eTIV','nWBV','ASF','CDR','GENDER','Targets'"


with st.expander("Features_Targets"):

  X = new_df.drop(['MR Delay','Targets'], axis=1)
  st.write("**X**")
  X


  st.write("**y**")
  y = new_df['Targets']
  y







