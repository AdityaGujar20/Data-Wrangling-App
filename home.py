import streamlit as st
import pandas as pd

# Function to load custom CSS
def load_custom_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load and apply the custom CSS
load_custom_css("custom.css")

# Main Streamlit app content
st.title("Understand your data in one click")
st.write("<div class='centered-bold-text'>Upload a CSV file</div>", unsafe_allow_html=True)

# upload_file = st.file_uploader("Choose the CSV file", type='.csv')
upload_file = st.file_uploader(label = '', type='.csv')


if upload_file is not None:
    
    
    st.write("<div class='centered-bold-text'>Original Data Preview</div>", unsafe_allow_html=True)
    df = pd.read_csv(upload_file)
    st.write(df.sample(5))
    

    st.write("<div class='centered-bold-text'>Shape of the data</div>", unsafe_allow_html=True)
    shape = df.shape
    shape_dic = {
        'Number of rows': shape[0],
        'Number of columns': shape[1]
    }
    
    st.dataframe(shape_dic)

    
    
    st.write("<div class='centered-bold-text'>Total number of null values by each column</div>", unsafe_allow_html=True)
    null_df = df.isnull().sum().reset_index()
    null_df.columns = ['Column Name', 'Number of Null Values']
    st.dataframe(null_df.set_index('Column Name'))

    st.write("<div class='centered-bold-text'>Descriptive Statistics</div>", unsafe_allow_html=True)
    st.write(df.describe())
    
    st.write("<div class = 'centered-bold-text'>Pearson's Correlation</div>", unsafe_allow_html=True)
    numeric_df = df.select_dtypes(include='number')
    st.write(numeric_df.corr())

