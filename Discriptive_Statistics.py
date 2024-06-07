import streamlit as st
import pandas as pd

def load_custom_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_custom_css("styles/styles.css")

st.title("Understand Your Data in One Click 👆🏽")

upload_file = st.file_uploader(label = '', type='.csv')
st.write("<hr>", unsafe_allow_html=True)

if upload_file is not None:
        
    st.write("<div class='centered-bold-text'>Original Data Snapshot</div>", unsafe_allow_html=True)
    df = pd.read_csv(upload_file)
    st.write(df.sample(5))
    st.write("<hr>", unsafe_allow_html=True)

    st.write("<div class='centered-bold-text'>Shape of the data</div>", unsafe_allow_html=True)
    shape = df.shape
    shape_dic = {
        'Number of rows': shape[0],
        'Number of columns': shape[1]
    }
    st.dataframe(shape_dic)
    st.write("<hr>", unsafe_allow_html=True)

    st.write("<div class='centered-bold-text'>Total number of missing values in each column</div>", unsafe_allow_html=True)
    null_df = df.isnull().sum().reset_index()
    null_df.columns = ['Column Name', 'Number of Null Values']
    st.dataframe(null_df.set_index('Column Name'))
    st.write("<hr>", unsafe_allow_html=True)

    st.write("<div class='centered-bold-text'>Descriptive Statistics</div>", unsafe_allow_html=True)
    st.write(df.describe())
    st.write("<hr>", unsafe_allow_html=True)
    
    st.write("<div class = 'centered-bold-text'>Pearson's Correlation</div>", unsafe_allow_html=True)
    st.write("1 means there is a positive correlation")
    st.write("0 means there is no correlation")
    st.write("-1 means there is a negatively correlation")
    numeric_df = df.select_dtypes(include='number')
    st.write(numeric_df.corr())
    st.write("<hr>", unsafe_allow_html=True)