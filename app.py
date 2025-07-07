# here we are writing some code of streamlit to learn git. 

import streamlit as st


st.title('CampusX')

col1, col2 = st.columns(2)
with col1: 
    st.image('unnamed.png')
with col2: 
    st.write("""
                A Machine Learning course can equip you with valuable skills for the future. It covers foundational concepts like supervised, unsupervised, and reinforcement learning, along with practical applications in areas like image/speech recognition and autonomous vehicles. Expect to learn about data analysis, model building, and evaluation techniques using tools like Python and relevant libraries.
                Introduction to Machine Learning: Understanding the fundamentals and types of ML (supervised, unsupervised, reinforcement learning). 
                Data Preprocessing: Cleaning, transforming, and preparing data for ML algorithms. 

                """)
    
    st.header('Course Offered')
    st.subheader('Data Science')
    st.subheader('Data Analysis')
    st.subheader('Data Engineering')
    st.subheader('MERN Stack')
    st.subheader('Backend Developemnt')

    st.subheader('These changes are only show in the main branch.')