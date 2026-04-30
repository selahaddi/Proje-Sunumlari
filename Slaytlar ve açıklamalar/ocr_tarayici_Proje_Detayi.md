# OCR Tarayıcı: Yapay Zeka Destekli Not Derleyici

## 📌 Proje Özeti
Bu proje, telefonla çekilmiş dağınık el yazısı notlarını, karışık ders fotoğraflarını veya taranmış PDF belgelerini dijital, düzenlenebilir ve net bir dokümana dönüştüren bir masaüstü yazılımıdır. "Stellar OCR & Note Compiler" olarak adlandırılan bu araç, kullanıcıya iki farklı motor seçeneği sunar: Karmaşık el yazıları için yüksek doğruluklu Google Gemini AI veya internetsiz ücretsiz kullanım için Tesseract OCR.

## 🚀 Temel Özellikler
- **Çift OCR (Optik Karakter Tanıma) Motoru Seçimi:**
  - **Google Gemini 1.5 Flash:** Bulut tabanlıdır. Kötü el yazılarını mükemmel okur, matematiksel formülleri tanıyıp LaTeX formatına ($x^2 + y$) çevirebilir.
  - **Tesseract OCR:** Çevrimdışı (offline) çalışır. Standart matbu metinler için çok hızlıdır, ücretsizdir ve API kotası gerektirmez.
- **Otomatik Toplu Derleme:** Seçtiğiniz bir klasörün içindeki onlarca fotoğrafı veya PDF'lerin her sayfasını sırayla okur. Sonunda tüm metinleri birleştirerek tek, düzenli bir `Ders_Notlari.pdf` (ve bir Markdown dosyası) üretir.
- **Akıllı Hata Düzeltme Filtresi:** Yabancı OCR modellerinin Türkçe karakterlerde sıkça yaptığı tipik "ii yerine ü", "g yerine ğ" gibi okuma hatalarını otomatik bulan ve düzelten bir filtre mekanizmasına sahiptir.
- **Asenkron Çalışma:** Arka planda ağır okuma işlemleri (Threading) yaparken masaüstü arayüzü donmaz. Ekranda anlık hangi sayfanın tarandığı detaylı bir LOG (kayıt) penceresinde akarak gösterilir.

## 🛠️ Kullanılan Teknolojiler
- **Görsel Arayüz (GUI):** Python `tkinter`
- **Metin Tanıma:** `google-generativeai` (Gemini API Entegrasyonu) ve `pytesseract` (Açık kaynak OCR motoru)
- **Görüntü ve Belge İşleme:** 
  - `Pillow` (Resim kütüphanesi)
  - `PyMuPDF` (`fitz` - PDF sayfalarını yüksek çözünürlüklü görsellere dönüştürmek için)
  - `fpdf` (Okunan metinleri nihai ve şık bir PDF raporuna basmak için)

## 📁 Proje Dosya Yapısı
- `ocr_gui.py`: Uygulamanın tüm işlemlerini yapan ana çekirdek (kod) dosyası. Arayüzün çizimi, resimlerin işlenmesi ve API'lerle iletişim buradadır.
- `tessdata/`: Çevrimdışı çalışan Tesseract motorunun karakterleri doğru tanıyabilmesi için ihtiyaç duyduğu eğitim verilerini (.traineddata dosyaları) içeren klasör.
- `.env`: Gemini API anahtarı veya Tesseract kurulu dizin gibi hassas ayarların gizli tutulduğu ortam değişkeni dosyası.
- `run_app.bat`: Teknik bilgiye sahip olmayan kullanıcıların, siyah terminal ekranlarıyla uğraşmadan uygulamayı çift tıklayarak açmasını sağlayan kısa komut dosyası.

## ⚙️ Nasıl Çalışır? (Sistem Akışı)
1. **Hazırlık:** Kullanıcı `run_app.bat` ile programı açar. İhtiyacına göre Gemini AI veya Tesseract arasından seçim yapar (Gemini için bir kereye mahsus API Key kaydedilir).
2. **Seçim:** Karmaşık notların bulunduğu "Girdi Klasörü" seçilir.
3. **Analiz (OCR Süreci):** "TARAMAYI BAŞLAT" butonuyla sistem devreye girer. Tüm resim ve PDF'ler arka planda tek tek yapay zekaya veya Tesseract motoruna iletilip sadece içlerindeki metinler çekilir.
4. **Formatlama:** Çıkarılan metinler başlıklandırılır, düzeltilir ve Markdown formatına getirilerek geçici bir ".md" dosyasında alt alta birleştirilir.
5. **Nihai Çıktı:** Markdown dosyası sisteme dahil edilen Türkçe uyumlu bir font yardımıyla (`fpdf`) tek ve derli toplu bir PDF belgesine dönüştürülüp hedef klasöre teslim edilir.
