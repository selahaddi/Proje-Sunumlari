# N8N Borsa: AI Destekli Hisse Senedi Analiz Platformu

## 📌 Proje Özeti
N8N Borsa projesi; borsa verilerini takip eden, teknik göstergeleri (RSI, MACD vb.) hesaplayan ve yapay zeka (Google Gemini) yardımıyla hisseleri yorumlayan gelişmiş bir finansal otomasyon sistemidir. Proje gücünü N8N'in sunduğu otomasyon yeteneklerinden alırken, kullanıcılara Next.js ile geliştirilmiş modern bir web paneli sunmaktadır. Ek olarak, detaylı borsa analiz raporlarını periyodik olarak e-posta üzerinden de iletebilmektedir.

## 🚀 Temel Özellikler
- **Geniş Çaplı Hisse Takibi:** Sisteme tanımlanmış 31 farklı hisse senedinin piyasa verilerini izleme.
- **AI ile Finansal Analiz:** Google Gemini entegrasyonu sayesinde, sayısal finansal veriler ve piyasa haberleri harmanlanarak insan dilinde yatırımcı öngörüleri üretilmesi.
- **Teknik Gösterge Hesaplamaları:** Hisselerin alım-satım sinyallerini tespit etmek için RSI, MACD ve Bollinger Bantları gibi popüler teknik indikatörlerin otomatik analizi.
- **Görsel Raporlama:** QuickChart servisinden yararlanılarak hisse hareketlerini ve teknik analiz verilerini görsel grafiklere dönüştürme.
- **Akıllı E-Posta Bülteni:** Yatırımcıya (veya kullanıcıya) n8n otomasyonu üzerinden, görseller ve AI analizleriyle zenginleştirilmiş hisse senedi bültenleri gönderme.
- **Modern Web Arayüzü (Dashboard):** Analizleri anlık olarak sorgulayıp inceleyebileceğiniz duyarlı (responsive) Next.js tabanlı arayüz.

## 🛠️ Kullanılan Teknolojiler
- **Frontend (Kullanıcı Arayüzü):** Next.js (React), Tailwind CSS
- **Backend & Otomasyon Süreçleri:** N8N (İş akışları, Webhook entegrasyonları, JavaScript kod blokları)
- **API ve Servisler:**
  - Google Gemini API (Yapay zeka yorumlaması)
  - NewsAPI (Güncel finans haberleri)
  - QuickChart (Dinamik grafik üretimi)

## 📁 Proje Klasör Yapısı
- `stock-analysis-web/`: Yatırımcıların hisse özetlerini ve analizlerini okuduğu Next.js tabanlı ön yüz klasörü.
- `Hisse.json`, `Stock List API.json`, `Stock Analysis API.json`: N8N sistemine doğrudan yüklenebilecek iş akışı (workflow) şablonları. Bu dosyalar veri çekme, işleme ve e-posta atma görevlerini yürütür.
- `webhook_*.js`: N8N içindeki "Code Node" kısımlarında çalışan özel veri işleme betikleri.
- `start_frontend.bat`: Next.js uygulamasını (`npm run dev`) Windows üzerinden tek tıklamayla ayağa kaldıran script.
- `Kurulum_Dosyaları/` & `Stock_Experiment/`: N8N kurulum adımlarını, test rehberlerini (`test_guide.md`, `n8n_webhook_setup.md`) ve deneme çalışmalarını barındıran dizinler.

## ⚙️ Nasıl Çalışır? (Sistem Akışı)
1. **N8N Kurulumu:** Gerekli `.json` uzantılı iş akışları n8n'e aktarılır, webhook'lar aktifleştirilir ve Gemini/NewsAPI anahtarları sisteme tanımlanır.
2. **Arayüzün Başlatılması:** `start_frontend.bat` ile Next.js ayağa kaldırılır.
3. **Veri Talebi:** Kullanıcı web arayüzüne (`localhost:3000`) girdiğinde veya bir hisseye tıkladığında, frontend n8n webhook'larına bir tetikleyici istek (HTTP Request) atar.
4. **Veri Toplama ve Yorumlama:** n8n bu isteği alır, hisse verilerini günceller, haberleri çeker, göstergeleri hesaplar ve veriyi Gemini'ye vererek "Bu hisse alınır mı/satılır mı?" sorusuna mantıklı bir yanıt üretmesini ister.
5. **Sonuç:** AI yorumu, grafik URL'leri ve ham finansal veriler, arayüze geri dönerek kullanıcıya detaylı bir yatırım analiz ekranı olarak sunulur. Ayrıca yapılandırılmışsa bir e-posta bülteni olarak gönderilir.
