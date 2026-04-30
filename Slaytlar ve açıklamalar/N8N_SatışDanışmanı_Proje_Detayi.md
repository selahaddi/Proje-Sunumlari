# N8N Satış Danışmanı: Akıllı B2B Teklif Hazırlama ve Takip Sistemi

## 📌 Proje Özeti
Bu proje; B2B (İşletmeden İşletmeye) formatında çalışan firmaların web üzerinden aldıkları sipariş veya fiyat teklifi taleplerini tamamen otomatize eden bir sistemdir. Gelen müşteri taleplerini otomatik olarak hesaplar, kurumsal bir PDF teklifine dönüştürür, müşteriye e-posta ile iletir ve yanıt alınamayan teklifler için (örneğin 3 gün sonra) satış temsilcisine Telegram üzerinden "satışı kapatması" için uyarı gönderir.

## 🚀 Temel Özellikler
- **Formdan Gelen Veriyi Anında İşleme:** Müşterilerin girdiği veriler (firma adı, ürün, adet) n8n üzerinden saniyeler içinde yakalanır ve veritabanına kaydedilir.
- **Dinamik ve Kurumsal PDF Üretimi:** Talepler, sabit bir metin yerine arka planda (Python yardımıyla) hesaplanarak özel bir HTML şablonuna gömülür ve profesyonel görünümlü bir PDF dosyasına çevrilir.
- **Tam Otomatik Müşteri Geri Dönüşü:** Oluşturulan fiyat teklifi (PDF), SMTP üzerinden otomatik olarak müşterinin e-posta adresine yollanır ve veritabanında o işin durumu "Cevap Bekleniyor" olarak güncellenir.
- **Satış Kapatma Takibi (Follow-up):** Her gün sabah 09:00'da çalışan bir zamanlayıcı, e-posta atılıp üzerinden 3 gün geçen ama hala kapanmayan işleri bulur ve şirketin satış danışmanına Telegram üzerinden "X firmasını ara, fiyat teklifini takip et" şeklinde akıllı uyarı atar.

## 🛠️ Kullanılan Teknolojiler
- **İş Akışı ve Otomasyon:** n8n 
- **Arka Plan Servisleri (Backend):** Python, FastAPI (n8n ile haberleşen yerel API sunucusu)
- **Veritabanı:** Supabase (PostgreSQL tabanlı bulut veritabanı)
- **Döküman Üretimi:** Jinja2 (HTML Şablon Motoru), `pdfkit` / `wkhtmltopdf` (PDF Dönüştürücü)
- **İletişim Servisleri:** Gmail SMTP (E-posta), Telegram Bot API
- **Kullanıcı Arayüzü:** HTML, CSS, Vanilla JS

## 📁 Proje Dosya Yapısı
- `app.py`: n8n'in isteklerini anında yakalamak için sürekli çalışan (FastAPI) köprü niteliğindeki sunucu uygulaması.
- `pdf_generator.py`: Gelen JSON verilerindeki ürün adetleriyle fiyatları çarpıp, sonuçları `templates/proposal_template.html` dosyasına işleyerek şık bir PDF basan Python modülü.
- `email_sender.py`: Üretilen PDF'i alıp müşteriye yollayan ve Supabase veritabanında "E-posta gönderildi" güncellemesi yapan script.
- `followup_reminder.py`: Veritabanında zaman aşımına uğramış "Cevap Bekleniyor" statüsündeki talepleri bulup Telegram botu ile satış personeline mesaj atan uyarıcı modül.
- `workflows/`: n8n'e direkt import edilebilecek olan 1. Teklif Kabul ve 2. Hatırlatıcı json şablonları.
- `start_server.bat`: Geliştirme ortamında Python FastAPI sunucusunu tek tıkla (`uvicorn`) ayağa kaldıran araç.

## ⚙️ Sistem Nasıl Çalışıyor? (Adım Adım)
1. **Talep Girişi:** Müşteri `index.html` üzerinden "Teklif İste" formunu doldurur ve veriler n8n Webhook'una POST edilir.
2. **Kayıt:** n8n, veriyi anında Supabase'e kaydeder.
3. **PDF Üretimi ve Gönderim:** Kayıt işleminden sonra n8n, yerel Python sunucusuna (app.py) bir sinyal yollar. Python, arka planda HTML tabanlı PDF'i yaratır ve bunu müşteriye e-posta ile ulaştırır.
4. **Zamanlanmış Hatırlatma (Cron):** Ertesi günlerde sabah 09:00'da n8n uyanır, Python'u tetikler. Python Supabase'i tarayarak "bekleyenleri" bulur ve "Satışı kapat!" uyarısıyla Telegram'a mesaj gönderir.
