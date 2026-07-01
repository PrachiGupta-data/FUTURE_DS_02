
# LOAD THE DATASET


import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="Customer Retention & Churn Analysis",
    page_icon="📊",
    layout="wide"
)

# Dashboard Title
st.title("📊 Customer Retention & Churn Analysis Dashboard")
st.write("This dashboard analyzes customer churn and retention patterns.")


# Load Dataset
DATA_PATH = "Dataset/Telco-Customer-Churn.csv"

df = pd.read_csv(DATA_PATH)

# Display Dataset
st.subheader("📋 Dataset Preview")
st.dataframe(df.head())

# Dataset Shape
st.subheader("📏 Dataset Shape")

rows, columns = df.shape

col1, col2 = st.columns(2)

with col1:
    st.metric("Total Rows", rows)

with col2:
    st.metric("Total Columns", columns)

# Column Names
st.subheader("📝 Column Names")

st.write(df.columns.tolist())

