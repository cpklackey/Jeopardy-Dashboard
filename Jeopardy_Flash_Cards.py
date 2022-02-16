import streamlit as st
import pandas as pd
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt

  
data =  pd.read_csv('jp_keywords.csv')

data.set_index('answer', inplace = True)
st.sidebar.header("Word Cloud Generator")
sample_list = data.index.sort_values()
##st.session_state.sample_list = sample_list
answer = st.sidebar.selectbox('Display Word Cloud for which Jeopardy Answer?', sample_list)
##st.sidebar.button('Refresh List')
if not st.sidebar.checkbox("Close", True, key='3'):
 
    st.subheader('Word Cloud for %s' % (answer))
    
    processed_words = data[data.index == answer]['keywords'][0]
  
    wordcloud = WordCloud(width = 600,prefer_horizontal=0.7, height = 400, random_state=1, background_color='black', colormap='Set2', collocations=False).generate(processed_words)
# Display the generated image
    fig, ax = plt.subplots()
    plt.imshow(wordcloud)
    plt.axis("off")
    st.pyplot(fig)
  