from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
chat = client.chats.create(model="gemini-2.0-flash")

# URL sources untuk MySkill learning paths
URL_SOURCES = {
    "home" : "https://myskill.id/",
    "e-learning": "https://myskill.id/e-learning",
    "paket video e learning 12 bulan":"https://myskill.id/payment/e-learning/zGgyeWtC6KQo2uAWetBR",
    "paket video e learning 6 bulan":"https://myskill.id/payment/e-learning/47qOozJUVg6zMNbCYzMv",
    "paket video e learning 1 bulan":"https://myskill.id/payment/e-learning/VXjsithqZKzHsPIXQfBn",
    "data science": "https://myskill.id/learning-path/data-science-and-data-analysis",
    "ui ux": "https://myskill.id/learning-path/ui-ux-research-design", 
    "web development": "https://myskill.id/learning-path/web-development",
    "ai": "https://myskill.id/learning-path/artificial-intelligence",
    "iot": "https://myskill.id/learning-path/internet-of-things",
    "web3": "https://myskill.id/learning-path/web-3-blockchain-development",
    "digital marketing": "https://myskill.id/learning-path/digital-marketing",
    "microsoft office":"https://myskill.id/learning-path/microsoft-excel-word-powerpoint",
    "product dan project management":"https://myskill.id/learning-path/product-project-management",
    "software quality assurance":"https://myskill.id/learning-path/software-quality-assurance",
    "english test":"https://myskill.id/learning-path/english-test-scholarship",
    "accounting":"https://myskill.id/learning-path/accounting-finance-tax",
    "human resource":"https://myskill.id/learning-path/human-resource-development",
    "sales, business development, and customer service":"https://myskill.id/learning-path/sales-and-business-development",
    "graphic design":"https://myskill.id/learning-path/graphic-design",
    "career & self development":"https://myskill.id/learning-path/career-and-self-development",
    "bisnis, online shop dan freelance":"https://myskill.id/learning-path/bisnis-online-shop-freelance",
    "foreign languages":"https://myskill.id/learning-path/foreign-languages"
}

def find_relevant_url(prompt):
    """Cari URL MySkill yang relevan dengan prompt"""
    prompt_lower = prompt.lower()
    
    # Cek apakah ada kata kunci learning path dalam prompt
    for topic, url in URL_SOURCES.items():
        if topic in prompt_lower or topic.replace(" ", "") in prompt_lower:
            return topic, url
    
    return None, None

def chat_bot(prompt):
    """Fungsi chat bot dengan informasi MySkill"""
    # Cari URL yang relevan
    topic, url = find_relevant_url(prompt)
    
    # Buat system prompt untuk Gemini
    system_prompt = f'''
        Anda adalah MySkill Learning Assistant, bot yang membantu pengguna memahami learning path di MySkill.id.
        
        Berikut adalah daftar learning path yang Anda ketahui beserta URL-nya:
        {chr(10).join([f"- {t.upper()}: {u}" for t, u in URL_SOURCES.items()])}
        
        Tugas Anda adalah:
        1. Menjawab pertanyaan pengguna tentang learning path MySkill.
        2. Jika pertanyaan pengguna cocok dengan salah satu learning path di atas, berikan informasi singkat tentang learning path tersebut dan **sertakan URL lengkapnya**.
        3. Jika pertanyaan tidak spesifik, tawarkan untuk menjelaskan learning path yang tersedia.
        4. Gunakan bahasa Indonesia yang ramah dan mudah dimengerti.
        5. Jangan tampilkan informasi yang tidak relevan atau terlalu panjang.
        '''
    
    # Gabungkan system prompt dengan pertanyaan user
    full_prompt = f"{system_prompt}\n\nPertanyaan User: {prompt}"
    
    try:
        response = chat.send_message(full_prompt)
        return response.text
    except Exception as e:
        print(f"Error in chat_bot: {e}")
        return "Maaf, terjadi kesalahan saat memproses permintaan Anda. Silakan coba lagi."