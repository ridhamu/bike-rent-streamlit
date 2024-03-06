import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set_theme(style='dark')
bike_df = pd.read_csv('bike_df.csv')

st.header('Bike Sharing Dataset 🚲 🚲 🚲')

st.subheader('Tingkat penyewaan sesuai dengan cuaca')

avg_weather = bike_df.groupby('weather_label')['cnt_day'].mean().reset_index().sort_values("cnt_day")

fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='cnt_day', y='weather_label', data=avg_weather, palette='viridis', ax=ax)

plt.title('Rata - Rata Penyewaan Sepeda berdasarkan Kondisi Cuaca')
plt.xlabel('Rata - Rata Penyewaan')
plt.ylabel('Kondisi Cuaca')

st.pyplot(fig)  # Menampilkan plot pertama dalam web dashboard

# Menampilkan subheader dan chart kedua
st.subheader('Rata-Rata Penyewaan Sepeda per Jam')

rental_jam = bike_df.groupby('hr')['cnt_hour'].mean()

fig2, ax2 = plt.subplots(figsize=(10, 6))
plt.bar(rental_jam.index, rental_jam.values, color='#1f77b4')

plt.title('Rata - Rata Penyewaan per Jam')
plt.xlabel('Jam')
plt.ylabel('Rata - Rata Penyewaan')

st.pyplot(fig2)  # Menampilkan plot kedua dalam web dashboard

# Menampilkan subheader dan chart ketiga
st.subheader('Hubungan Hari Libur dengan Penyewaan Sepeda')

avg_holiday = bike_df.groupby('holiday_day')['cnt_day'].mean().reset_index().sort_values("cnt_day")

fig3, ax3 = plt.subplots(figsize=(8, 5))
sns.barplot(x='holiday_day', y='cnt_day', data=avg_holiday, palette='Set2', ax=ax3)

plt.title('Rata-rata Penyewaan Sepeda pada Hari Libur')
plt.xlabel('Hari Libur')
plt.ylabel('Rata-rata Penyewaan')
plt.xticks([0, 1], ['Tidak Libur', 'Libur'])

st.pyplot(fig3)  # Menampilkan plot ketiga dalam web dashboard
