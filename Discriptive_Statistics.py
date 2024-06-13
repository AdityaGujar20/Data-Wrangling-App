import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from wordcloud import WordCloud

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
    
    st.write("<div class = 'centered-bold-text'>Pearson's Correlation Heatmap</div>", unsafe_allow_html=True)   
    st.markdown("**Understanding Correlation:**")
    st.markdown("- **1**: Strong positive correlation")
    st.markdown("- **0**: No correlation")
    st.markdown("- **-1**: Strong negative correlation")
    numeric_df = df.select_dtypes(include='number')
    corr_matrix = numeric_df.corr().round(2)
    fig = px.imshow(corr_matrix, 
                    x=corr_matrix.index, 
                    y=corr_matrix.columns, 
                    color_continuous_scale='Viridis',
                    labels=dict(color="Correlation")
                )
    fig.update_layout(
        width=800,
        height=600,
        title='Correlation Heatmap',
        title_x=0.5, 
        xaxis_title='Features',
        yaxis_title='Features',
        font=dict(size=12), 
        coloraxis_colorbar=dict(
            title='Correlation',
            tickvals=[-1, 0, 1],  
            ticktext=['-1 (Negative)', '0 (None)', '1 (Positive)'],
        )
    )
    st.plotly_chart(fig)
    st.write("<hr>", unsafe_allow_html=True)
    
    # Interactive Scatter Plot
    st.write("<div class = 'centered-bold-text'>Interactive Scatter Plot</div>", unsafe_allow_html=True)
    x_axis = st.selectbox('Select X-axis:', options=numeric_df.columns, index=0)
    y_axis = st.selectbox('Select Y-axis:', options=numeric_df.columns, index=1)
    fig = px.scatter(data_frame=df, x=x_axis, y=y_axis)
    fig.update_layout(
        width=800,
        height=600,
        xaxis_title=x_axis,
        yaxis_title=y_axis,
        font=dict(size=12),
    )
    st.plotly_chart(fig)
    st.write("<hr>", unsafe_allow_html = True)