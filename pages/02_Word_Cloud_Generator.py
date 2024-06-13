import streamlit as st
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def load_custom_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_custom_css("styles/styles.css")

st.title('Categorical Data Word Cloud Generator ☁️')
uploaded_file = st.file_uploader(label= "", type="csv")
st.write("<hr>", unsafe_allow_html=True)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
    selected_column = st.selectbox('Select a column:', options=[''] + categorical_cols)
    if selected_column and df is not None:
        def generate_wordcloud(text):
            wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.imshow(wordcloud, interpolation='bilinear')
            ax.axis('off')
            st.pyplot(fig)
        text_data = ' '.join(df[selected_column].dropna().astype(str))
        generate_wordcloud(text_data)
