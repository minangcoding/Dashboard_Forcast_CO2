""" 
Fungsi slider() pada Streamlit digunakan untuk membuat widget slider interaktif yang 
memungkinkan pengguna untuk memilih nilai dalam rentang tertentu. Slider ini sangat 
berguna ketika Anda ingin mengizinkan pengguna memilih angka dalam rentang tertentu 
(misalnya, untuk memilih nilai numerik, tahun, atau durasi) secara dinamis.
"""
# st.slider(label, min_value=None, max_value=None, value=None, step=None, format=None, key=None, help=None)
#Parameter:
#label: Teks yang akan ditampilkan di samping slider. Ini adalah parameter wajib.
# min_value: Nilai minimum yang dapat dipilih pada slider (defaultnya adalah nilai minimum dari rentang).
# max_value: Nilai maksimum yang dapat dipilih pada slider (defaultnya adalah nilai maksimum dari rentang).
# value: Nilai default yang akan ditampilkan pada slider saat pertama kali dimuat (bisa berupa tuple jika ingin nilai awal untuk rentang).
# step: Langkah (step size) untuk slider. Nilai default adalah 1, tetapi bisa diubah sesuai kebutuhan.
# format: Format penampilan nilai yang dipilih, biasanya digunakan untuk angka (misalnya, "%d" untuk angka bulat).
# key: Kunci unik untuk widget ini (berguna jika Anda membuat banyak widget dengan nama yang sama).
# help: Tooltip yang ditampilkan saat pengguna mengarahkan kursor ke slider.

# Contoh Penggunaan:
# Slider untuk memilih nilai tunggal:

import streamlit as st

# Membuat slider
value = st.slider("Pilih angka", min_value=1, max_value=100, value=50)

st.write(f"Anda memilih {value}")

# Slider untuk memilih rentang nilai: Anda juga dapat mengonfigurasi slider untuk memilih rentang angka.
import streamlit as st

# Membuat slider untuk rentang
value_range = st.slider("Pilih rentang usia", min_value=0, max_value=100, value=(20, 50))

st.write(f"Usia yang dipilih: {value_range[0]} - {value_range[1]}")

#Slider dengan langkah tertentu: 
# Misalnya, jika Anda ingin langkah slider adalah 5 
# (misalnya untuk memilih kelipatan 5), Anda dapat menetapkan parameter step:

import streamlit as st

# Membuat slider dengan langkah 5
value = st.slider("Pilih kelipatan 5", min_value=5, max_value=100, step=5, value=50)

st.write(f"Anda memilih {value}")

"""

Pada Python atau Streamlit, penggunaan columns([2, 3]) biasanya merujuk pada penataan atau 
pengaturan tata letak kolom dalam tampilan. Dalam konteks Streamlit, columns() adalah fungsi 
untuk membagi halaman aplikasi menjadi beberapa kolom, memungkinkan elemen-elemen untuk ditata 
secara paralel atau berdampingan.

Namun, penggunaan columns([2, 3]) tidak secara langsung terhubung dengan sintaks Streamlit. 
Kemungkinan besar, yang dimaksud adalah pemanggilan fungsi st.columns() yang digunakan untuk 
membagi halaman menjadi beberapa kolom.

Penjelasan tentang st.columns() pada Streamlit:
st.columns() digunakan untuk membuat beberapa kolom di dalam aplikasi Streamlit. 
Fungsi ini mengembalikan beberapa kolom yang bisa digunakan untuk menempatkan berbagai elemen, 
seperti teks, gambar, grafik, dan sebagainya dalam kolom terpisah. 
"""
"""
  columns = st.columns([2, 3])

"""

"""
Pada contoh di atas:

1. [2, 3]: Parameter ini menentukan proporsi lebar kolom. Kolom pertama akan memiliki ukuran relatif 2 dan 
kolom kedua akan memiliki ukuran relatif 3. Dengan cara ini, kolom pertama akan lebih sempit dibandingkan dengan kolom kedua.

2. st.columns([2, 3]) mengembalikan dua kolom yang bisa Anda isi dengan komponen atau widget.  
"""


import streamlit as st

# Membagi halaman menjadi dua kolom dengan proporsi 2 dan 3
col1, col2 = st.columns([2, 3])

with col1:
    st.header("Kolom 1")
    st.write("Ini adalah kolom pertama dengan ukuran lebih kecil.")

with col2:
    st.header("Kolom 2")
    st.write("Ini adalah kolom kedua dengan ukuran lebih besar.")
    

"""
Pada contoh di atas:

Kolom pertama (col1) memiliki ukuran lebih kecil (proporsi 2).
Kolom kedua (col2) memiliki ukuran lebih besar (proporsi 3). 
"""

"""
Fungsi:
columns([2, 3]): Ini digunakan untuk menentukan distribusi lebar antar kolom dalam aplikasi Streamlit.
Pembagian Tata Letak: Kolom ini memungkinkan Anda menata tampilan dengan cara yang lebih rapi dan responsif. 
Anda bisa menempatkan berbagai elemen di setiap kolom sesuai dengan kebutuhan tata letak Anda. 
"""
