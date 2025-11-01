import streamlit as st
from streamlit.components.v1 import html

# Sayfa ayarlarını yapılandırma.
st.set_page_config(
    page_title="Aşkım İçin ❤️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ----------------------------------------------------------------------
# DÜZELTME: HTML içeriği için Ham Dize (Raw String - r"""...""") kullanıldı
# ve CSS animasyonları, Python'ın yanlış yorumlama ihtimalini azaltmak
# için biraz daha sadeleştirildi.
# ----------------------------------------------------------------------
custom_html_content = r"""
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sonsuz Aşkımın Nedenleri</title>
    
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        /* Özelleştirilmiş Animasyon ve Renkler */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        /* Hata Çıkaran Pulse animasyonu kaldırıldı, sadece fadeIn bırakıldı */
        .reason-card {
            animation: fadeIn 0.8s ease-out;
        }

        /* Streamlit konteynerinin ortalanmasını sağlamak için ekstra stil */
        body {
            display: flex;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
        }
    </style>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        // Koyu Tonlar
                        'bg-navy': '#0F172A',         /* Ana Arka Plan (En Koyu) */
                        'bg-card-main': '#1E293B',    /* Merkezi Kart Arka Planı (Biraz Açık Koyu) */
                        'primary-text': '#F1F5F9',    /* Açık Metin Rengi */
                        'button-red': '#DC2626',      /* Buton Kırmızımsı (Aşk Teması) */
                        'button-red-hover': '#B91C1C', /* Buton Hover Kırmızısı */
                        'accent-border': '#475569',    /* Koyu Kart Sınırları */
                        'card-bg-light': '#F8FAFC',    /* Kart İç Arka Planı */
                        'text-dark': '#1E293B',        /* Kart İç Metin Rengi */
                    }
                }
            }
        }
    </script>
</head>
<body class="min-h-screen flex items-center justify-center p-4 bg-bg-navy" 
      style="font-family: 'Inter', sans-serif;">

    <!-- Ana Kart -->
    <div class="w-full max-w-lg mx-auto bg-bg-card-main p-8 sm:p-10 rounded-3xl shadow-2xl border border-accent-border">

        
        <h1 class="text-3xl font-extrabold text-button-red text-center mb-4">
            Seni Neden Mi Seviyorum? ❤️
        </h1>
        <p class="text-center text-primary-text mb-8">
            Aşağıdaki butona basarak sana olan sevgimin rastgele bir nedenini keşfet!
        </p>

        
        <button id="reasonButton"
                class="w-full py-4 px-6 bg-button-red text-white font-bold text-lg rounded-full 
                       shadow-lg shadow-button-red/50 hover:bg-button-red-hover transition duration-300 transform hover:scale-[1.02] 
                       focus:outline-none focus:ring-4 focus:ring-button-red/50">
            Yeni Bir Neden Keşfet! 💖
        </button>

        <hr class="my-8 border-t-2 border-accent-border">

        
        <div id="reasonDisplay" class="min-h-[120px] flex items-center justify-center">
            <p id="initialMessage" class="text-gray-400 italic text-center">
                Burada sana özel bir sevgi nedeni belirecek...
            </p>
        </div>

        
        <div class="mt-8 pt-4 border-t border-accent-border text-center">
            <p class="text-sm text-gray-400">(Her zaman seni düşünüyorum.)</p>
        </div>

    </div>

    <script>
        // --- SENİN ÖZEL SEVGİ NEDENLERİN ---
        const sevgiNedenleri = [
            "Gülüşünü seviyorum, bana dünyaları veriyor. 😊",
            "Yanımda olman, bana her zaman güç veriyor. 💪",
            "Zekana hayranım, her konuştuğumuzda yeni şeyler öğreniyorum. 🧠",
            "En sevdiğim rengin senin gözlerinin rengi olması. ✨",
            "Bana her zaman destek olmanı ve beni motive etmeni seviyorum. 🚀",
            "Küçük sürprizlerin ve düşünceli hallerin beni mutlu ediyor. 🎁",
            "Seninle geçirdiğim her anın değerli olması. ⏳",
            "Bana hissettirdiğin güven duygusu. 🛡️",
            "Birlikte saçmalamayı ve kahkahalar atmayı seviyorum. 😂",
            "Hayallerime inanmanı ve beni desteklemeni seviyorum. 🌟",
            "Sabah uyandığımda aklıma ilk gelen kişi olman. ☀️",
            "Her zaman beni dinlemen ve anlamaya çalışman. 👂",
            "En zor zamanlarımda bile yanımda olman. 🫂",
            "Seninle olmak, en sevdiğim yer olmak demek. 🏡",
            "Hayatıma kattığın pozitif enerji ve neşe. 🎈",
            "Bana hissettirdiğin eşsiz aşk duygusu. ❤️",
            "Her detayı düşünerek beni şaşırtman. 🤔",
            "Sesini duymak, günümü güzelleştiriyor. 🎶",
            "Yanında kendim olabildiğim tek yer. 🧘",
            "Birlikte sessizliğin bile anlamlı olması. 🤫",
            "En kötü günümde bile beni güldürebilmen. 😄",
            "Sana her baktığımda kalbimin hızlı atması. 💓",
            "Birlikte kahve içmek bile seninle güzel. ☕",
            "Hayatıma anlam katmanı seviyorum. 🌈",
            "Bana kendimi özel hissettirmen. 💎",
            "Her zorluğa seninle göğüs gerebileceğimi bilmem. ⛰️",
            "Senden her gün yeni bir şey öğreniyorum. 💡"
        ];

        const reasonDisplay = document.getElementById('reasonDisplay');
        const initialMessage = document.getElementById('initialMessage');
        const reasonButton = document.getElementById('reasonButton');

        function getRandomReason() {
            // Rastgele bir neden seç
            const randomIndex = Math.floor(Math.random() * sevgiNedenleri.length);
            const reason = sevgiNedenleri[randomIndex];

            // Sonuç Kartı HTML'ini oluştur
            const reasonCardHTML = `
                <div class="reason-card bg-card-bg-light p-6 rounded-xl border-4 border-button-red/50 shadow-lg w-full max-w-md">
                    <p class="text-text-dark text-xl sm:text-2xl font-semibold italic mb-3 text-gray-800">
                        "${reason}"
                    </p>
                    <p class="text-sm text-gray-500 mt-4">
                        Seni ∞ seviyorum! 💖
                    </p>
                </div>
            `;
            
            // Eski içeriği temizle ve yeni kartı ekle
            reasonDisplay.innerHTML = reasonCardHTML;
        }

        // Buton olay dinleyicisini ekle
        reasonButton.addEventListener('click', getRandomReason);
    </script>
</body>
</html>
"""

# HTML içeriğini Streamlit'te göster.
html(custom_html_content, height=700, scrolling=True)

# Streamlit'in kendi bileşenlerini kullanarak ek bilgi eklemek
st.markdown("---")
st.info("Bu, Streamlit'in özel bileşeni (`st.components.v1.html`) ile gömülmüş, tamamen özel HTML/CSS/JavaScript içeriğidir.")
