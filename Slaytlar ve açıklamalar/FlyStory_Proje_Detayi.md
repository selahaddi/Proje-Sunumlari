# FlyStory: Modern Havacılık Keşif Platformu

## 📌 Proje Özeti
FlyStory, havacılık meraklıları için özel olarak geliştirilmiş, uçak modellerini, teknik verilerini ve anlık telemetri bilgilerini sunan görsel odaklı, tam donanımlı (Full-Stack) bir web uygulamasıdır. Arka planda yüksek performanslı Go (Golang) kullanılırken, ön yüzde React ve Tailwind CSS ile son derece modern, estetik ve akıcı bir kullanıcı deneyimi sunulmaktadır.

## 🚀 Temel Özellikler
- **Modern ve Estetik Arayüz:** Google Stitch'ten ilham alınan, "Mesh-Gradient" arka planlar ve "Glassmorphism" (cam efekti) barındıran şık tasarım.
- **Canlı Telemetri Simülasyonu:** Uçakların irtifa (altitude), hız (speed) ve koordinat (enlem/boylam) bilgilerini gerçek zamanlı olarak saniyede bir güncelleyerek harita/gösterge verilerini besleyen Go tabanlı arka plan motoru.
- **Gelişmiş Komut Paleti (Command Palette):** Tıpkı modern editörlerde olduğu gibi `⌘ K` (veya `Ctrl + K`) klavye kısayoluyla açılan hızlı arama modülü.
- **Akıllı Arama ve API Entegrasyonu:**
  - Uçak markaları (Boeing, Airbus, Cessna vb.) için yerleşik veritabanında hızlı arama.
  - Özel bir algoritma sayesinde girilen uçuş numaralarından (örn: TK1923, FR5325) uçak modellerini tahmin etme yeteneği.
  - Eksik uçak bilgileri için dış bir havacılık API'sine anlık olarak bağlanıp veri çekme özelliği.

## 🛠️ Kullanılan Teknolojiler
- **Frontend (Kullanıcı Arayüzü):** 
  - **React & Vite:** Çok hızlı derleme ve komponent tabanlı geliştirme altyapısı.
  - **Tailwind CSS v4:** Modern ve responsif tasarım.
  - **Framer Motion:** Kullanıcı etkileşimleri ve sayfa geçişleri için akıcı animasyonlar.
- **Backend (Veri ve Sunucu):** 
  - **Go (Golang):** Hızlı ve verimli API uç noktaları (`/api/aircrafts`, `/api/search`, `/api/telemetry`).
  - **Goroutines:** Ana akışı dondurmadan arka planda sürekli veri (telemetri) üretmek için kullanılan asenkron mimari.

## 📁 Proje Mimari Yapısı
- `main.go` & `internal/`: Go sunucusunun çekirdeğini oluşturan, yönlendirmeleri yapan ve veritabanı ile (iç/dış) etkileşime giren backend klasörleri.
- `src/`: React frontend'ine ait bileşenler, sayfalar ve global CSS dosyaları.
- `tasarim.html` & `code.html`: Projenin yapım aşamasında referans alınan statik UI tasarımları.
- `baslat.bat`: Windows kullanıcıları için tek tıkla hem Go (Port: 8080) hem de Vite (Port: 5173) sunucularını aynı anda başlatan, ardından tarayıcıyı açan başlatma dosyası.

## ⚙️ Sistem Akışı
1. Kullanıcı `baslat.bat` ile projeyi ayaklandırır.
2. Web arayüzü açıldığında, Go backend'i anlık telemetri verisi yayınlamaya başlar.
3. Kullanıcı arama çubuğuna bir model veya uçuş numarası yazar. Go sunucusu bu metni analiz eder; ya yerel veritabanından, ya da harici API'den sonucu bulup saniyeler içinde ön yüze iletir.
4. Çekilen uçak verisi ve anlık değişen yükseklik/hız değerleri, animasyonlu cam efektli kartlarda kullanıcıya gösterilir.
