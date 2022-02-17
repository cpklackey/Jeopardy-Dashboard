import streamlit as st
import pandas as pd
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt


data =  pd.read_csv('jp_keywords.csv')
data.drop_duplicates(subset=['answer'],inplace = True)
data.set_index('answer', inplace = True)
st.sidebar.header("Word Cloud Generator")
sample_list = list(data.index.sort_values())
##st.session_state.sample_list = sample_list
##start = '0'
##end = 'zurich'
start, end = st.sidebar.select_slider('Select a range of answers',
options=sample_list
,value=('0', 'zurich'),
format_func=lambda x: x[0]
)
answer = st.sidebar.selectbox('Display Word Cloud for which Jeopardy Answer?', sample_list[sample_list.index(start):sample_list.index(end)])
##st.sidebar.button('Refresh List')
if not st.sidebar.checkbox("Close", True, key='3'):
    
 
    st.subheader('Word Cloud for "%s"' % (answer))
    
    processed_words = data[data.index == answer]['keywords'][0]
  
    wordcloud = WordCloud(width = 600,prefer_horizontal=0.7, height = 400, random_state=1, background_color='black', colormap='Set2', collocations=False).generate(processed_words)
# Display the generated image
    fig, ax = plt.subplots()
    plt.imshow(wordcloud)
    plt.axis("off")
    st.pyplot(fig)
  