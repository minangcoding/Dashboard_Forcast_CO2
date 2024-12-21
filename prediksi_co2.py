import pickle
import streamlit as st
import pandas as pd
import matplotlib.pylab as plt 

model = pickle.load(open("prediksi_terbaru_c02.sav", 'rb'))

df = pd.read_excel("CO2 dataset.xlsx")
df["Year"] = pd.to_datetime(df["Year"], format="%Y")
df.set_index(["Year"], inplace=True)

st.title("Forecasting Kualitas Udara")
year = st.slider("Tentukan Tahun ", 1,30, step=1)

""" 
Fungsi slider() pada Streamlit digunakan untuk membuat widget slider interaktif yang 
memungkinkan pengguna untuk memilih nilai dalam rentang tertentu. Slider ini sangat 
berguna ketika Anda ingin mengizinkan pengguna memilih angka dalam rentang tertentu 
(misalnya, untuk memilih nilai numerik, tahun, atau durasi) secara dinamis.
"""

pred = model.forecast(year)
pred = pd.DataFrame(pred, columns=["CO2"]) # colum co2

# logika
if st.button("Predict"):
    col1, col2 = st.columns([2,3])
    with col1:
        st.dataframe(pred)
    
    with col2:
        fig, ax = plt.subplots()
        df["CO2"].plot(style="--", color="gray", legend=True, label="Known")
        pred["CO2"].plot(color="b", legend=True, label="Prediction") # hasilmprediski
        st.pyplot(fig)