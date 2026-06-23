import streamlit as st

# Pengaturan halaman
st.set_page_config(page_title="Kalkulator BMI", page_icon="⚖️")

def hitung_bmi(berat, tinggi):
    return berat / (tinggi ** 2)

def kategori_bmi(bmi):
    if bmi < 18.5:
        return "Kekurangan berat badan (Underweight)", "yellow"
    elif 18.5 <= bmi < 24.9:
        return "Berat badan normal (Healthy)", "green"
    elif 25 <= bmi < 29.9:
        return "Kelebihan berat badan (Overweight)", "orange"
    else:
        return "Obesitas (Obesity)", "red"

# Tampilan UI
st.title("⚖️ Kalkulator BMI")
st.write("Masukkan data Anda di bawah ini untuk mengetahui status berat badan Anda.")

col1, col2 = st.columns(2)

with col1:
    berat = st.number_input("Berat Badan (kg)", min_value=1.0, step=0.1, format="%.1f")
with col2:
    tinggi_cm = st.number_input("Tinggi Badan (cm)", min_value=50.0, step=1.0, format="%.1f")

if st.button("Hitung Sekarang"):
    if tinggi_cm > 0:
        tinggi_m = tinggi_cm / 100
        bmi = hitung_bmi(berat, tinggi_m)
        kategori, warna = kategori_bmi(bmi)
        
        st.divider()
        st.metric(label="Nilai BMI Anda", value=f"{bmi:.1f}")
        st.markdown(f"Status: :{warna}[**{kategori}**]")
    else:
        st.error("Tinggi badan harus lebih dari 0!")

# Footer sederhana
st.markdown("---")
st.caption("Aplikasi ini dibuat sebagai alat bantu edukasi kesehatan.")
