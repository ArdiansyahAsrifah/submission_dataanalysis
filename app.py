import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
file_path = 'datasets/day.csv'
df = pd.read_csv(file_path)

# Konversi kolom tanggal ke datetime jika belum
df['dteday'] = pd.to_datetime(df['dteday'])

# Set kolom 'dteday' sebagai indeks
df.set_index('dteday', inplace=True)

# Konversi indeks ke kolom untuk penggunaan berikutnya
df['dteday'] = df.index

# Set style for plots
sns.set(style="whitegrid")
plt.rcParams['figure.figsize'] = (14, 8)

# Sidebar
st.sidebar.title('Dashboard Menu')

# Menambahkan menu dropdown untuk memilih visualisasi
menu = ['Daily Trend', 'Weekly Trend', 'Monthly Trend', 'Comparison']
choice = st.sidebar.selectbox('Choose Visualization', menu)

# Main content
st.title('Bike Sharing Analysis')

if choice == 'Daily Trend':
    st.header('Daily Trend of Bike Rentals')

    # Resampling data untuk tren harian
    daily_trend = df['cnt'].resample('D').sum()

    # Plot tren harian
    st.line_chart(daily_trend)

elif choice == 'Weekly Trend':
    st.header('Weekly Trend of Bike Rentals')

    # Resampling data untuk tren mingguan
    weekly_trend = df['cnt'].resample('W').sum()

    # Plot tren mingguan
    st.line_chart(weekly_trend)

elif choice == 'Monthly Trend':
    st.header('Monthly Trend of Bike Rentals')

    # Resampling data untuk tren bulanan
    monthly_trend = df['cnt'].resample('M').sum()

    # Plot tren bulanan
    st.line_chart(monthly_trend)

elif choice == 'Comparison':
    st.header('Comparison Between Weekday and Weekend Bike Rentals')

    # Menambah kolom baru untuk menandai hari kerja atau akhir pekan
    df['day_type'] = df['dteday'].apply(lambda x: 'Weekend' if x.dayofweek in [0, 6] else 'Weekday')

    # Boxplot untuk melihat distribusi jumlah total peminjaman berdasarkan jenis hari
    st.write(df.groupby('day_type')['cnt'].describe())

    # Tampilkan boxplot
    fig, ax = plt.subplots()
    sns.boxplot(data=df, x='day_type', y='cnt', ax=ax)
    ax.set_title('Total Bike Rentals by Day Type (Weekday vs Weekend)')
    ax.set_xlabel('Day Type')
    ax.set_ylabel('Total Rentals')
    st.pyplot(fig)

# Tampilkan informasi tambahan
st.markdown("""
    * **Daily Trend**: Menampilkan tren harian penggunaan sepeda berbagi.
    * **Weekly Trend**: Menampilkan tren mingguan penggunaan sepeda berbagi.
    * **Monthly Trend**: Menampilkan tren bulanan penggunaan sepeda berbagi.
    * **Comparison**: Membandingkan penggunaan sepeda berbagi antara hari kerja dan akhir pekan.
""")
