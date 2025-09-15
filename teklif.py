<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>İlişki Testi</title>
    <!-- Tailwind CSS'i CDN üzerinden dahil ediyoruz -->
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;800&display=swap');
        body {
            font-family: 'Inter', sans-serif;
            transition: background-color 0.5s ease;
        }

        /* Giriş ve sonuç içeriği için animasyon */
        .fade-in {
            animation: fadeIn 1.5s ease-in-out forwards;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .shake {
            animation: shake 0.5s cubic-bezier(.36,.07,.19,.97) both;
            transform: translate3d(0, 0, 0);
            backface-visibility: hidden;
            perspective: 1000px;
        }

        @keyframes shake {
            10%, 90% { transform: translate3d(-1px, 0, 0); }
            20%, 80% { transform: translate3d(2px, 0, 0); }
            30%, 50%, 70% { transform: translate3d(-4px, 0, 0); }
            40%, 60% { transform: translate3d(4px, 0, 0); }
        }

        .deny-animation {
            animation: moveAround 1s cubic-bezier(.25,.8,.5,1) forwards;
        }

        @keyframes moveAround {
            0% { transform: translateX(0); }
            20% { transform: translateX(-20px); }
            40% { transform: translateX(20px); }
            60% { transform: translateX(-10px); }
            80% { transform: translateX(10px); }
            100% { transform: translateX(0); }
        }
        
        .pulse {
            animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
        }
        @keyframes pulse {
            0%, 100% {
                transform: scale(1);
            }
            50% {
                transform: scale(1.05);
            }
        }
    </style>
</head>
<body class="bg-gray-950 text-white flex items-center justify-center min-h-screen p-4">

    <!-- Başlangıç Ekranı -->
    <div id="baslangic-ekrani" class="text-center max-w-lg w-full transition-opacity duration-1000 ease-in-out">
        <h1 class="text-4xl md:text-5xl font-extrabold mb-8 drop-shadow-lg text-rose-400">
            Aşkın İki Yüzü
        </h1>
        <p class="text-lg md:text-xl text-gray-300 mb-8">
            İlişkimizin bu iki önemli anında, sen hangisini seçerdin?
        </p>
        
        <div class="flex flex-col sm:flex-row justify-center items-center gap-6">
            <button id="zor-gun-butonu" class="bg-gray-700 hover:bg-gray-600 text-white font-bold py-3 px-8 rounded-full shadow-lg transition-all duration-300 transform hover:scale-105 focus:outline-none focus:ring-4 focus:ring-gray-500">
                <i class="fas fa-cloud-sun mr-2"></i> Zor Bir Günde
            </button>
            
            <button id="karar-an-butonu" class="bg-gray-700 hover:bg-gray-600 text-white font-bold py-3 px-8 rounded-full shadow-lg transition-all duration-300 transform hover:scale-105 focus:outline-none focus:ring-4 focus:ring-gray-500">
                <i class="fas fa-brain mr-2"></i> Önemli Bir Karar Alırken
            </button>
        </div>
    </div>

    <!-- Zor Gün Seçim Ekranı -->
    <div id="zor-gun-ekrani" class="hidden opacity-0 text-center max-w-xl w-full transition-opacity duration-1000 ease-in-out">
        <h2 class="text-3xl md:text-4xl font-bold mb-8 text-white fade-in">
            Zor Bir Günde Ona Nasıl Destek Olursun?
        </h2>
        
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 fade-in mb-8">
            <button class="secenek-butonu bg-gray-700 hover:bg-gray-600 text-white font-bold py-3 px-8 rounded-full shadow-lg transition-all duration-300 transform hover:scale-105" data-sonuc-id="sonuc-1">
                <i class="fas fa-hand-holding-heart mr-2"></i> Yanında Olmak
            </button>
            <button class="secenek-butonu bg-gray-700 hover:bg-gray-600 text-white font-bold py-3 px-8 rounded-full shadow-lg transition-all duration-300 transform hover:scale-105" data-sonuc-id="sonuc-1">
                <i class="fas fa-person-shelter mr-2"></i> Alan Tanımak
            </button>
            <button class="secenek-butonu bg-gray-700 hover:bg-gray-600 text-white font-bold py-3 px-8 rounded-full shadow-lg transition-all duration-300 transform hover:scale-105" data-sonuc-id="sonuc-1">
                <i class="fas fa-headphones mr-2"></i> Sadece Dinlemek
            </button>
        </div>

        <button id="zor-gun-sonuc-butonu" class="hidden mt-8 bg-rose-600 hover:bg-rose-700 text-white font-bold py-4 px-10 rounded-full shadow-lg transition-all duration-300 transform hover:scale-110 focus:outline-none focus:ring-4 focus:ring-rose-500">
            Sonucu Gör
        </button>
    </div>

    <!-- Karar Anı Seçim Ekranı -->
    <div id="karar-ekrani" class="hidden opacity-0 text-center max-w-xl w-full transition-opacity duration-1000 ease-in-out">
        <h2 class="text-3xl md:text-4xl font-bold mb-8 text-white fade-in">
            Önemli Bir Karar Alırken Ona Nasıl Destek Olursun?
        </h2>
        
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 fade-in mb-8">
            <button class="secenek-butonu bg-gray-700 hover:bg-gray-600 text-white font-bold py-3 px-8 rounded-full shadow-lg transition-all duration-300 transform hover:scale-105" data-sonuc-id="sonuc-2">
                <i class="fas fa-comments mr-2"></i> Tüm Olasılıkları Konuşmak
            </button>
            <button class="secenek-butonu bg-gray-700 hover:bg-gray-600 text-white font-bold py-3 px-8 rounded-full shadow-lg transition-all duration-300 transform hover:scale-105" data-sonuc-id="sonuc-2">
                <i class="fas fa-handshake mr-2"></i> Seçimine Güvenmek
            </button>
            <button class="secenek-butonu bg-gray-700 hover:bg-gray-600 text-white font-bold py-3 px-8 rounded-full shadow-lg transition-all duration-300 transform hover:scale-105" data-sonuc-id="sonuc-2">
                <i class="fas fa-star mr-2"></i> En İyisini İstediğini Bilmek
            </button>
        </div>

        <button id="karar-sonuc-butonu" class="hidden mt-8 bg-rose-600 hover:bg-rose-700 text-white font-bold py-4 px-10 rounded-full shadow-lg transition-all duration-300 transform hover:scale-110 focus:outline-none focus:ring-4 focus:ring-rose-500">
            Sonucu Gör
        </button>
    </div>

    <!-- Sonuç Ekranı -->
    <div id="sonuc-ekrani" class="hidden opacity-0 text-center max-w-lg w-full transition-opacity duration-1000 ease-in-out">
        <div class="flex flex-col items-center justify-center">
            <i class="fas fa-heart text-5xl md:text-7xl text-rose-500 mb-6 drop-shadow-lg animate-pulse-slow"></i>
            <h3 id="sonuc-baslik" class="text-3xl md:text-4xl font-bold mb-4 text-white fade-in"></h3>
            <p id="sonuc-mesaj" class="text-xl md:text-2xl text-gray-300 mb-8 fade-in"></p>
            <button id="date-proposal-butonu" class="mt-8 bg-pink-600 hover:bg-pink-700 text-white font-bold py-4 px-10 rounded-full shadow-lg transition-all duration-300 transform hover:scale-110 focus:outline-none focus:ring-4 focus:ring-pink-500">
                Son Bir Soru
            </button>
        </div>
    </div>

    <!-- Yeni Çıkma Teklifi Ekranı -->
    <div id="date-proposal-ekrani" class="hidden opacity-0 text-center max-w-lg w-full transition-opacity duration-1000 ease-in-out">
        <div class="flex flex-col items-center justify-center">
            <h3 class="text-4xl md:text-5xl font-extrabold mb-8 drop-shadow-lg text-rose-400 fade-in">
                Benimle çıkar mısın?
            </h3>
            <div class="flex justify-center items-center gap-6">
                <button id="evet-butonu" class="bg-green-600 hover:bg-green-700 text-white font-bold py-3 px-8 rounded-full shadow-lg transition-all duration-300 transform hover:scale-110 focus:outline-none focus:ring-4 focus:ring-green-500">
                    Evet
                </button>
                <button id="hayir-butonu" class="bg-red-900 text-white font-bold py-3 px-8 rounded-full shadow-lg">
                    Hayır
                </button>
            </div>
        </div>
    </div>

    <!-- Final Ekranı -->
    <div id="final-ekrani" class="hidden opacity-0 text-center max-w-lg w-full transition-opacity duration-1000 ease-in-out">
        <div class="flex flex-col items-center justify-center">
            <!-- Özel Mesajı Aç Butonu -->
            <button id="gizli-mesaj-butonu" class="bg-purple-600 hover:bg-purple-700 text-white font-bold py-4 px-10 rounded-full shadow-lg transition-all duration-300 transform hover:scale-110 focus:outline-none focus:ring-4 focus:ring-purple-500 pulse">
                <i class="fas fa-envelope-open-text mr-2"></i> Özel Mesaj
            </button>

            <!-- Gizli Mesaj Kutusu (Başlangıçta gizli) -->
            <div id="gizli-mesaj-kutusu" class="hidden mt-8 bg-gray-800 p-8 rounded-xl shadow-xl border border-gray-700 fade-in">
                <i class="fas fa-heart text-5xl md:text-7xl text-rose-500 mb-6 drop-shadow-lg animate-pulse-slow"></i>
                <h3 class="text-3xl md:text-4xl font-bold mb-4 text-white fade-in">
                    Sadece Sen...
                </h3>
                <p class="text-xl md:text-2xl text-gray-300 mb-8 fade-in">
                    Tüm bu karmaşık soruların tek bir cevabı var: Sen. Her an, her zorlukta, her kararda... Kalbim hep seninle. Seni çok seviyorum. <br>
                    <br>
                    <span class="text-rose-400 font-bold">(<span class="cursor-pointer">Faruğu</span> engelle)</span>
                </p>
            </div>
        </div>
    </div>

    <script>
        // DOM elemanlarını seçme
        const zorGunButonu = document.getElementById('zor-gun-butonu');
        const kararAnButonu = document.getElementById('karar-an-butonu');
        const secenekButonlari = document.querySelectorAll('.secenek-butonu');
        const zorGunSonucButonu = document.getElementById('zor-gun-sonuc-butonu');
        const kararSonucButonu = document.getElementById('karar-sonuc-butonu');
        const dateProposalButonu = document.getElementById('date-proposal-butonu');
        const evetButonu = document.getElementById('evet-butonu');
        const hayirButonu = document.getElementById('hayir-butonu');
        const gizliMesajButonu = document.getElementById('gizli-mesaj-butonu');
        const gizliMesajKutusu = document.getElementById('gizli-mesaj-kutusu');
        
        const baslangicEkrani = document.getElementById('baslangic-ekrani');
        const zorGunEkrani = document.getElementById('zor-gun-ekrani');
        const kararEkrani = document.getElementById('karar-ekrani');
        const sonucEkrani = document.getElementById('sonuc-ekrani');
        const dateProposalEkrani = document.getElementById('date-proposal-ekrani');
        const finalEkrani = document.getElementById('final-ekrani');

        const sonucBaslik = document.getElementById('sonuc-baslik');
        const sonucMesaj = document.getElementById('sonuc-mesaj');

        // Sonuç mesajları
        const sonucMetinleri = {
            "sonuc-1": {
                baslik: "İlişkimizdeki Güç!",
                mesaj: "Zor zamanlarda yanında olmak, sana alan tanımak veya sadece dinlemek... Hangi yolu seçersem seçeyim, senin için en doğru desteği sağlamak benim için önemli. Birlikteyken her zorluğun üstesinden geliriz."
            },
            "sonuc-2": {
                baslik: "İlişkimizdeki Uyum!",
                mesaj: "Önemli kararları birlikte almak, seçimine güvenmek... Hangi yolu seçersem seçeyim, benim için en önemli şey senin mutluluğun ve huzurun. Hayat yolunda en doğru kararları beraber veririz."
            }
        };

        // Sayfa geçişlerini yöneten fonksiyon
        const showScreen = (currentScreen, nextScreen) => {
            currentScreen.classList.add('opacity-0');
            setTimeout(() => {
                currentScreen.classList.add('hidden');
                nextScreen.classList.remove('hidden');
                setTimeout(() => {
                    nextScreen.classList.remove('opacity-0');
                }, 50);
            }, 1000);
        };

        // Seçenek butonlarının tıklama olayını dinleme
        secenekButonlari.forEach(buton => {
            buton.addEventListener('click', () => {
                const parentGrid = buton.closest('.grid');
                if (parentGrid) {
                    parentGrid.querySelectorAll('.secenek-butonu').forEach(btn => {
                        btn.classList.remove('bg-blue-600', 'hover:bg-blue-700');
                        btn.classList.add('bg-gray-700', 'hover:bg-gray-600');
                    });
                }
                
                buton.classList.remove('bg-gray-700', 'hover:bg-gray-600');
                buton.classList.add('bg-blue-600', 'hover:bg-blue-700');

                const parentScreen = buton.closest('#zor-gun-ekrani, #karar-ekrani');
                if (parentScreen) {
                    if (parentScreen.id === 'zor-gun-ekrani') {
                        zorGunSonucButonu.classList.remove('hidden');
                    } else if (parentScreen.id === 'karar-ekrani') {
                        kararSonucButonu.classList.remove('hidden');
                    }
                }
            });
        });

        // Başlangıç butonları
        zorGunButonu.addEventListener('click', () => {
            showScreen(baslangicEkrani, zorGunEkrani);
        });

        kararAnButonu.addEventListener('click', () => {
            showScreen(baslangicEkrani, kararEkrani);
        });

        // Sonuç butonları
        zorGunSonucButonu.addEventListener('click', () => {
            const sonucId = "sonuc-1";
            sonucBaslik.textContent = sonucMetinleri[sonucId].baslik;
            sonucMesaj.textContent = sonucMetinleri[sonucId].mesaj;
            showScreen(zorGunEkrani, sonucEkrani);
        });

        kararSonucButonu.addEventListener('click', () => {
            const sonucId = "sonuc-2";
            sonucBaslik.textContent = sonucMetinleri[sonucId].baslik;
            sonucMesaj.textContent = sonucMetinleri[sonucId].mesaj;
            showScreen(kararEkrani, sonucEkrani);
        });
        
        // Yeni butonun click handler'ı
        dateProposalButonu.addEventListener('click', () => {
            showScreen(sonucEkrani, dateProposalEkrani);
        });

        // Evet butonunun click handler'ı
        evetButonu.addEventListener('click', () => {
            showScreen(dateProposalEkrani, finalEkrani);
        });

        // Hayır butonuna basılınca animasyon ve tekrar tıklanamaz hale gelme
        hayirButonu.addEventListener('click', (e) => {
            e.preventDefault();
            e.stopPropagation(); 
            hayirButonu.classList.add('deny-animation');
            hayirButonu.classList.add('pointer-events-none');
            setTimeout(() => {
                hayirButonu.classList.remove('deny-animation');
            }, 1000); 
        });

        // Gizli mesajı açma butonu
        gizliMesajButonu.addEventListener('click', () => {
            gizliMesajButonu.classList.add('hidden');
            gizliMesajKutusu.classList.remove('hidden');
        });
    </script>
</body>
</html>
