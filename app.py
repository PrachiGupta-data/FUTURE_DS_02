# =====================================================
# IMPORT LIBRARIES
# =====================================================

import streamlit as st
import pandas as pd
import plotly.express as px

# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="Customer Retention & Churn Analysis",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Customer Retention & Churn Analysis Dashboard")
st.info("This dashboard helps identify churn risk customers and improve retention strategy.")
# =====================================================
# LOAD DATASET
# =====================================================



df = pd.read_csv("Telco-Customer-Churn.csv")


# =====================================================
# DATA CLEANING
# =====================================================

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Convert TotalCharges to numeric
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

# Fill missing values
df["TotalCharges"] = df["TotalCharges"].fillna(0)

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

# =====================================================
# FEATURE ENGINEERING
# =====================================================

# Customer Lifetime Value
df["CLV"] = df["MonthlyCharges"] * df["tenure"]

# Tenure Group
def tenure_group(tenure):
    if tenure <= 12:
        return "0-1 Year"
    elif tenure <= 24:
        return "1-2 Years"
    elif tenure <= 48:
        return "2-4 Years"
    elif tenure <= 60:
        return "4-5 Years"
    else:
        return "5+ Years"

df["TenureGroup"] = df["tenure"].apply(tenure_group)

# =====================================================
# SIDEBAR FILTERS
# =====================================================

st.sidebar.header("🔍 Filter Customers")

selected_gender = st.sidebar.multiselect(
    "Gender",
    options=sorted(df["gender"].unique()),
    default=sorted(df["gender"].unique())
)

selected_contract = st.sidebar.multiselect(
    "Contract",
    options=sorted(df["Contract"].unique()),
    default=sorted(df["Contract"].unique())
)

selected_internet = st.sidebar.multiselect(
    "Internet Service",
    options=sorted(df["InternetService"].unique()),
    default=sorted(df["InternetService"].unique())
)

selected_payment = st.sidebar.multiselect(
    "Payment Method",
    options=sorted(df["PaymentMethod"].unique()),
    default=sorted(df["PaymentMethod"].unique())
)

selected_senior = st.sidebar.multiselect(
    "Senior Citizen",
    options=sorted(df["SeniorCitizen"].unique()),
    default=sorted(df["SeniorCitizen"].unique())
)

# =====================================================
# APPLY FILTERS
# =====================================================

filtered_df = df[
    (df["gender"].isin(selected_gender)) &
    (df["Contract"].isin(selected_contract)) &
    (df["InternetService"].isin(selected_internet)) &
    (df["PaymentMethod"].isin(selected_payment)) &
    (df["SeniorCitizen"].isin(selected_senior))
]

# =====================================================
# KPI CALCULATIONS
# =====================================================

total_customers = len(filtered_df)

churned_customers = filtered_df[filtered_df["Churn"] == "Yes"].shape[0]

retained_customers = filtered_df[filtered_df["Churn"] == "No"].shape[0]

if total_customers == 0:
    churn_rate = retention_rate = avg_monthly_charges = avg_tenure = avg_clv = 0
else:
    churn_rate = (churned_customers / total_customers) * 100
    retention_rate = (retained_customers / total_customers) * 100
    avg_monthly_charges = filtered_df["MonthlyCharges"].mean()
    avg_tenure = filtered_df["tenure"].mean()
    avg_clv = filtered_df["CLV"].mean()

# =====================================================
# KPI CARDS
# =====================================================


row1_col1, row1_col2, row1_col3, row1_col4 = st.columns(4)

with row1_col1:
    st.metric("👥 Total Customers", f"{total_customers:,}")

with row1_col2:
    st.metric("❌ Churned Customers", f"{churned_customers:,}")

with row1_col3:
    st.metric("✅ Retained Customers", f"{retained_customers:,}")

with row1_col4:
    st.metric("📉 Churn Rate", f"{churn_rate:.2f}%")

row2_col1, row2_col2, row2_col3, row2_col4 = st.columns(4)

with row2_col1:
    st.metric("📈 Retention Rate", f"{retention_rate:.2f}%")

with row2_col2:
    st.metric("💵 Avg Monthly Charges", f"${avg_monthly_charges:.2f}")

with row2_col3:
    st.metric("⏳ Avg Tenure", f"{avg_tenure:.2f} Months")

with row2_col4:
    st.metric("💰 Avg Customer Lifetime Value", f"${avg_clv:.2f}")

st.markdown("---")

# =====================================================
# VISUALIZATIONS
# =====================================================

st.subheader("📊 Customer Churn Analysis")

# -------------------------
# Row 1
# -------------------------

col1, col2 = st.columns(2)

with col1:

    churn_counts = (
        filtered_df["Churn"]
        .value_counts()
        .reset_index()
    )

    churn_counts.columns = ["Churn", "Customers"]

    fig = px.pie(
        churn_counts,
        names="Churn",
        values="Customers",
        hole=0.5,
        title="Customer Churn Distribution",
        color="Churn",
        color_discrete_map={
            "Yes": "red",
            "No": "green"
        }
    )

    st.plotly_chart(fig, use_container_width=True)


with col2:

    contract = (
        filtered_df.groupby(["Contract", "Churn"])
        .size()
        .reset_index(name="Customers")
    )

    fig = px.bar(
        contract,
        x="Contract",
        y="Customers",
        color="Churn",
        barmode="group",
        title="Contract Type vs Churn"
    )

    st.plotly_chart(fig, use_container_width=True)

# -------------------------
# Row 2
# -------------------------

col3, col4 = st.columns(2)

with col3:

    internet = (
        filtered_df.groupby(["InternetService", "Churn"])
        .size()
        .reset_index(name="Customers")
    )

    fig = px.bar(
        internet,
        x="InternetService",
        y="Customers",
        color="Churn",
        title="Internet Service vs Churn",
        barmode="group"
    )

    st.plotly_chart(fig, use_container_width=True)


with col4:

    payment = (
        filtered_df.groupby(["PaymentMethod", "Churn"])
        .size()
        .reset_index(name="Customers")
    )

    fig = px.bar(
        payment,
        x="PaymentMethod",
        y="Customers",
        color="Churn",
        title="Payment Method vs Churn",
        barmode="group"
    )

    fig.update_layout(xaxis_tickangle=-20)

    st.plotly_chart(fig, use_container_width=True)

# -------------------------
# Row 3
# -------------------------

col5, col6 = st.columns(2)

with col5:

    tenure = (
        filtered_df.groupby(["TenureGroup", "Churn"])
        .size()
        .reset_index(name="Customers")
    )

    fig = px.bar(
    tenure,
    x="TenureGroup",
    y="Customers",
    color="Churn",
    title="Customer Churn by Tenure Group",
    barmode="group",
    category_orders={
        "TenureGroup": [
            "0-1 Year",
            "1-2 Years",
            "2-4 Years",
            "4-5 Years",
            "5+ Years"
        ]
    }
)

    st.plotly_chart(fig, use_container_width=True)


with col6:

    fig = px.histogram(
        filtered_df,
        x="MonthlyCharges",
        color="Churn",
        nbins=30,
        title="Monthly Charges Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

# -------------------------
# Full Width Chart
# -------------------------

fig = px.histogram(
    filtered_df,
    x="tenure",
    color="Churn",
    nbins=30,
    title="Customer Tenure Distribution"
)

st.plotly_chart(fig, use_container_width=True)
st.markdown("---")

gender = filtered_df["gender"].value_counts().reset_index()
gender.columns = ["Gender", "Customers"]

fig = px.bar(
    gender,
    x="Gender",
    y="Customers",
    title="Customer Distribution by Gender",
    text="Customers"
)

fig.update_layout(
    xaxis_title="Gender",
    yaxis_title="Number of Customers"
)

st.plotly_chart(fig, use_container_width=True)

# Highest churn by Contract
highest_churn_contract = (
    filtered_df.groupby("Contract")["Churn"]
    .apply(lambda x: (x == "Yes").mean() * 100)
    .idxmax()
)

# Highest churn by Internet Service
highest_churn_internet = (
    filtered_df.groupby("InternetService")["Churn"]
    .apply(lambda x: (x == "Yes").mean() * 100)
    .idxmax()
)

# =====================================================
# BUSINESS INSIGHTS
# =====================================================
st.markdown("---")
st.subheader("💡 Business Insights")

st.info(f"Overall churn rate: {churn_rate:.2f}%")

st.success(f"Average customer tenure: {avg_tenure:.1f} months")

st.success(f"Average Customer Lifetime Value (CLV): ${avg_clv:.2f}")

st.warning(f"Highest churn contract type: {highest_churn_contract}")

st.warning(f"Highest churn internet service: {highest_churn_internet}")

st.error("Key Risk: Month-to-Month customers with high monthly charges are most likely to churn")
# =====================================================
# RECOMMENDATIONS
# =====================================================

st.markdown("---")
st.subheader("🚀 Recommendations")

st.success("""
✅ Encourage Month-to-Month customers to switch to longer contracts.

✅ Provide loyalty rewards for customers with low tenure.

✅ Monitor customers with high monthly charges.

✅ Promote automatic payment methods.

✅ Focus retention campaigns on high-risk customer segments.
""")


# =====================================================
# FOOTER
# =====================================================

st.markdown("---")

st.caption(
    "Built using Streamlit, Pandas, Plotly Express"
)

