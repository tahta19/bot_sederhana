import streamlit as st
from inference import chat_bot, URL_SOURCES

# Header
st.title("📚 MySkill Learning Assistant")
st.write("Temukan learning path yang tepat untuk kariermu di MySkill.id")

# Inisialisasi Chat 
if "messages" not in st.session_state:
    st.session_state.messages = []

# Pisahkan URL_SOURCES menjadi kategori
PAKET_ELEARNING = {
    "Paket Video E-Learning 12 Bulan": "paket video e learning 12 bulan",
    "Paket Video E-Learning 6 Bulan": "paket video e learning 6 bulan", 
    "Paket Video E-Learning 1 Bulan": "paket video e learning 1 bulan"
}

ELEARNING_PATHS = {
    "Data Science": "data science",
    "UI/UX Design": "ui ux",
    "Web Development": "web development",
    "Artificial Intelligence": "ai",
    "Internet of Things": "iot",
    "Web3 & Blockchain": "web3",
    "Digital Marketing": "digital marketing",
    "Microsoft Office": "microsoft office",
    "Product & Project Management": "product dan project management",
    "Software Quality Assurance": "software quality assurance",
    "English Test": "english test",
    "Accounting": "accounting",
    "Human Resource": "human resource",
    "Sales, Business Development, Customer Service": "sales, business development, and customer service",
    "Graphic Design": "graphic design",
    "Career & Self Development": "career & self development",
    "Bisnis, Online Shop & Freelance": "bisnis, online shop dan freelance",
    "Foreign Languages": "foreign languages"
}

# Function untuk handle dropdown selection
def handle_paket_selection():
    if st.session_state.paket_dropdown != "-- Pilih Paket --":
        selected = st.session_state.paket_dropdown
        paket_key = PAKET_ELEARNING[selected]
        prompt = f"Ceritakan tentang {paket_key}"
        
        # Menambahkan pesan dari user
        st.session_state.messages.append({
            "role": "user", 
            "content": prompt
        })
        
        # respon bot
        response = chat_bot(prompt)
        
        # asisten
        st.session_state.messages.append({
            "role": "assistant", 
            "content": response
        })

def handle_path_selection():
    if st.session_state.path_dropdown != "-- Pilih Learning Path --":
        selected = st.session_state.path_dropdown
        path_key = ELEARNING_PATHS[selected]
        prompt = f"Ceritakan tentang learning path {path_key}"
        
        # Menambahkan pesan dari user
        st.session_state.messages.append({
            "role": "user", 
            "content": prompt
        })
        
        # Respon bot
        response = chat_bot(prompt)
        
        # asisten 
        st.session_state.messages.append({
            "role": "assistant", 
            "content": response
        })

# Tampilkan welcome message jika belum ada chat
if len(st.session_state.messages) == 0:
    st.write("### Selamat datang!")
    st.write("""
    Saya adalah MySkill Learning Assistant yang akan membantu Anda menemukan learning path yang tepat. 
    
    **Cara menggunakan:**
    - Pilih paket atau learning path dari dropdown di bawah
    - Atau ketik pertanyaan langsung di chat
    """)

# Dropdown di area utama
st.write("### Pilih Kategori")

col1, col2 = st.columns(2)

with col1:
    st.subheader("💳 Paket E-Learning")
    selected_paket = st.selectbox(
        "Pilih paket berlangganan:",
        ["-- Pilih Paket --"] + list(PAKET_ELEARNING.keys()),
        key="paket_dropdown",
        on_change=handle_paket_selection
    )

with col2:
    st.subheader("📚 E-Learning Path")
    selected_path = st.selectbox(
        "Pilih learning path:",
        ["-- Pilih Learning Path --"] + list(ELEARNING_PATHS.keys()),
        key="path_dropdown",
        on_change=handle_path_selection
    )

# Tampilkan semua URL yang tersedia
with st.expander("Semua Link MySkill"):
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Paket E-Learning:**")
        for name, key in PAKET_ELEARNING.items():
            url = URL_SOURCES[key]
            st.markdown(f"- [{name}]({url})")
    
    with col2:
        st.write("**Learning Paths:**")
        for name, key in ELEARNING_PATHS.items():
            url = URL_SOURCES[key]
            st.markdown(f"- [{name}]({url})")

# Tampilkan chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
prompt = st.chat_input("Ketik Pesan Disini")

if prompt:
    # User ngirim chat
    with st.chat_message("user"):
        st.markdown(prompt)
    
    st.session_state.messages.append({
        "role": "user", 
        "content": prompt
    })
    
    # Dapatkan respons dari bot
    with st.chat_message("assistant"):
        with st.spinner("Bot sedang berpikir..."):
            response = chat_bot(prompt)
        st.markdown(response)
    
    st.session_state.messages.append({
        "role": "assistant", 
        "content": response
    })

# Footer
st.markdown("---")
st.write("Powered by Google Gemini 2.0 • MySkill Learning Assistant")
