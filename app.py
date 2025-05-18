import streamlit as st
import pandas as pd
import string

# Load kamus dari CSV
@st.cache_data
def load_kamus():
    df = pd.read_csv("alay_dict.csv")
    return dict(zip(df['alay'], df['formal']))

alay_dict = load_kamus()

# Preprocessing
def preprocess(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text.split()

# Normalisasi`pip install streamlit

def normalize(tokens, kamus):
    return [kamus.get(word, word) for word in tokens]

# Streamlit UI
st.set_page_config(page_title="Text Normalizer", page_icon="🗣️")
st.title("🗣️ Text Normalizer: Bahasa Gaul ke Formal")
st.markdown("Masukkan kalimat tidak formal/gaul, lalu tekan normalisasi untuk melihat versi bahasanya yang formal.")

input_text = st.text_area("💬 Masukkan teks gaul:", "gw td lg d rmh trs ga bisa bales chat loe, sori yaa")

if st.button("🔄 Normalisasi"):
    tokens = preprocess(input_text)
    normalized_tokens = normalize(tokens, alay_dict)
    normalized_text = " ".join(normalized_tokens)

    st.subheader("✅ Hasil Normalisasi:")
    st.success(normalized_text)

    with st.expander("🔍 Lihat proses tokenisasi dan konversi"):
        st.write("Token Awal:", tokens)
        st.write("Token Setelah Normalisasi:", normalized_tokens)
