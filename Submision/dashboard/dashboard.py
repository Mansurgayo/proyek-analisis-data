import pandas as pd
import streamlit as st
import plotly.express as px


df = pd.read_csv('gabungan_day_hour.csv')


df['dteday'] = pd.to_datetime(df['dteday'])


day_mapping = {
    0: 'Senin', 1: 'Selasa', 2: 'Rabu', 3: 'Kamis', 
    4: 'Jumat', 5: 'Sabtu', 6: 'Minggu'
}
df['weekday'] = df['weekday'].map(day_mapping)


st.sidebar.title('📅 Filter Data')


available_years = sorted(df['dteday'].dt.year.unique())  
selected_year = st.sidebar.selectbox('Pilih Tahun', available_years)


df_year_filtered = df[df['dteday'].dt.year == selected_year]


min_date = df_year_filtered['dteday'].min().date()  
max_date = df_year_filtered['dteday'].max().date()  


selected_dates = st.sidebar.date_input('Pilih Rentang Tanggal selama 1 minggu', [min_date, max_date], min_value=min_date, max_value=max_date)

if isinstance(selected_dates, tuple):  
    start_date, end_date = selected_dates
else: 
    start_date = end_date = selected_dates  


start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)


df_filtered = df_year_filtered[(df_year_filtered['dteday'] >= start_date) & 
                               (df_year_filtered['dteday'] <= end_date)]


st.sidebar.subheader('📆 Pilih Hari')
available_days = df_filtered['weekday'].unique().tolist()
selected_days = st.sidebar.multiselect('Pilih Hari', available_days, default=available_days)


df_filtered = df_filtered[df_filtered['weekday'].isin(selected_days)]


st.title('📊 Dashboard Analisis Penyewaan Sepeda')

if not df_filtered.empty:
   
    st.subheader('📊 Tren Penggunaan Sepeda Berdasarkan Hari')
    day_trend = df_filtered.groupby('weekday')['cnt'].sum().reset_index()
    day_trend['weekday'] = pd.Categorical(day_trend['weekday'], categories=day_mapping.values(), ordered=True)
    day_trend = day_trend.sort_values('weekday')
    fig_day = px.bar(day_trend, x='weekday', y='cnt', title='Tren Penyewaan Sepeda per Hari', 
                     labels={'cnt': 'Jumlah Penyewa', 'weekday': 'Hari'}, color='weekday')
    st.plotly_chart(fig_day)

   
    st.subheader(' Penyewaan Sepeda Berdasarkan Jam')
    fig_hour = px.line(df_filtered, x='hr', y='cnt', color='weekday', markers=True, 
                       title='Jumlah Penyewa Sepeda berdasarkan Jam',
                       labels={'hr': 'Jam', 'cnt': 'Jumlah Penyewa', 'weekday': 'Hari'}, line_shape='spline')
    fig_hour.update_traces(line=dict(width=2))  # Bikin garis lebih tebal agar lebih jelas
    st.plotly_chart(fig_hour)

    
    st.subheader(' Jam dengan Penyewa Terbanyak')
    peak_hour = df_filtered.groupby('hr')['cnt'].sum().idxmax()
    peak_renters = df_filtered.groupby('hr')['cnt'].sum().max()
    st.write(f' **Puncak penyewaan terjadi pada jam {peak_hour}:00 dengan {peak_renters} penyewa.**')

else:
    st.write("Tidak ada data dalam rentang tanggal atau hari yang dipilih.")
