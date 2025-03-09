import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load dataset
df = pd.read_csv("C:/Users/Lenovo/Downloads/all_data.csv", parse_dates=["datetime"])

# Set title
st.title("Dashboard Kualitas Udara - Dongsi")

# Sidebar filters
st.sidebar.header("Filter Data")
start_date = st.sidebar.date_input("Mulai Tanggal", df["datetime"].min())
end_date = st.sidebar.date_input("Akhir Tanggal", df["datetime"].max())

# Filter data
df_filtered = df[(df["datetime"] >= str(start_date)) & (df["datetime"] <= str(end_date))]

# Show dataset
if st.sidebar.checkbox("Tampilkan Data", False):
    st.write(df_filtered.head())

# Visualisasi Tren PM2.5
st.subheader("Tren PM2.5 dari Waktu ke Waktu")
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(df_filtered["datetime"], df_filtered["PM2.5"], label="PM2.5", color='red')
ax.set_xlabel("Waktu")
ax.set_ylabel("PM2.5")
ax.legend()
st.pyplot(fig)

# Distribusi PM2.5
st.subheader("Distribusi PM2.5")
fig, ax = plt.subplots(figsize=(8, 4))
sns.histplot(df_filtered["PM2.5"], bins=30, kde=True, ax=ax)
st.pyplot(fig)

# Korelasi Faktor Cuaca dengan PM2.5
st.subheader("Korelasi PM2.5 dengan Faktor Cuaca")
weather_cols = ["TEMP", "PRES", "DEWP", "WSPM"]
fig = px.scatter_matrix(df_filtered, dimensions=weather_cols, color="PM2.5")
st.plotly_chart(fig)

# Visualisasi Polutan
st.subheader("Rata-rata Konsentrasi Polutan")
avg_pollutants = df_filtered[["PM2.5", "PM10", "SO2", "NO2", "CO", "O3"]].mean()
st.bar_chart(avg_pollutants)

# Wind Direction Analysis
st.subheader("Distribusi Arah Angin")
fig, ax = plt.subplots(figsize=(8, 4))
sns.countplot(x=df_filtered["wd"], order=df_filtered["wd"].value_counts().index, ax=ax)
st.pyplot(fig)

st.write("Dashboard ini menampilkan berbagai analisis terkait kualitas udara di Distrik Dongsi.")