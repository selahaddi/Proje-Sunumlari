# Şablon Oluşturma: Duvar Kağıdı (Wallpaper) Otomasyonu ve Satış Botu

## 📌 Proje Özeti
Bu proje, dijital sanatçıların veya içerik üreticilerinin tasarladığı yüzlerce duvar kağıdını (wallpaper) otomatik olarak estetik sunum şablonlarına (mockup) dönüştüren ve bunları "Buy Me a Coffee" platformuna dijital ürün olarak kendi kendine yükleyen çift yönlü bir otomasyon sistemidir. Görüntü işleme (Python PIL) ve tarayıcı otomasyonunu (Playwright) birleştirerek saatler sürecek manuel ürün yükleme işlemlerini dakikalara indirir.

## 🚀 Temel Özellikler
- **Toplu Görsel İşleme (Batch Processing):** Yüzlerce ham duvar kağıdını tarayarak ortası net, arkası flu (blur efektli), köşeleri yuvarlatılmış ve özel çerçeveli "sunum (mockup)" versiyonlarına dönüştürür.
- **Otomatik Dijital Ürün (ZIP) Hazırlama:** Satışa sunulacak yüksek çözünürlüklü duvar kağıtlarını her klasör için otomatik olarak analiz edip geçici bir `.zip` dosyası (ürün teslimat dosyası) haline getirir.
- **Buy Me a Coffee Otomasyon Botu:** Playwright kullanarak tarayıcıyı kontrol eder. Özel CSV listesindeki sıraya göre her ürün için:
  - Ürün başlığını (Title),
  - Fiyatını (Price),
  - Açıklamasını (Description),
  - Etiketlerini (Categories/Tags),
  - Hazırlanan ZIP dosyasını ve Kapak Fotoğrafını (Featured Image) platforma otomatik yükler.
- **Yarı Otonom Güvenlik (İnsan Onayı):** Bot, ürün taslağını %100 hazırladıktan sonra "Publish" (Yayınla) tuşuna basmaz. İnsan kontrolü ve son onayı için bekler. Onay verilince sıradaki ürüne geçer.
- **Kaldığı Yerden Devam Edebilme:** İnternet kopması veya hata durumunda, CSV listesindeki belirli bir satırdan (index) veya klasör isminden devam etme seçeneği sunar.

## 🛠️ Kullanılan Teknolojiler
- **Görüntü İşleme:** Python `Pillow` (PIL) kütüphanesi (Resim boyutlandırma, Gaussian Blur filtresi, katman (RGBA) maskeleme, köşe yuvarlatma).
- **Tarayıcı Otomasyonu (Web Botu):** `Playwright` (Açık kaynaklı, hızlı, oturum/çerezleri koruyan ve elementleri bekleme kapasitesine sahip modern tarayıcı aracı).
- **Veri Okuma:** `pandas` (Excel/CSV veritabanı yönetimi).
- **Dosya İşlemleri:** `os` ve `zipfile` (Sıkıştırma ve klasör tarama işlemleri).

## 📁 Proje Dosya Yapısı
- `batch_process.py`: Klasörlerdeki ham duvar kağıtlarının çerçeveli ve arkaplanı bulanık şık sunum (kapak) versiyonlarını üreten görüntü işleme betiği.
- `buy_me_a_coffee_uploader.py`: CSV tablosunu okuyup Playwright botu ile siteye dijital ürün (Extra) yüklemesi yapan asıl otomasyon kodu.
- `chrome_profile/` & `playwright_chrome_profile/`: Botun her seferinde yeniden giriş yapmaması için oturum (login) verilerinin/çerezlerinin güvenle saklandığı tarayıcı profili klasörleri.
- `wallpapers/`: Satılacak tüm duvar kağıtlarının klasörler halinde tutulduğu ve ürün isim/açıklamalarını barındıran `wallpaper_satis_listesi.csv` belgesinin bulunduğu ana veri dizini.
- `create_combos.py`: Birden fazla resmi yan yana birleştirip "kombo (kolaj)" kapak fotoğrafları üretmeye yarayan araç.

## ⚙️ Nasıl Çalışır? (Sistem Akışı)
1. **Görsel Hazırlık:** Kullanıcı `batch_process.py` betiğini çalıştırır. Sistem, klasörlerdeki duvar kağıtlarının sosyal medya ve mağaza kapak fotoğraflarını saniyeler içinde üretir.
2. **CSV Yapılandırması:** Yüklenecek ürünlerin isimleri, SEO uyumlu açıklamaları ve fiyatları CSV dosyasında tanımlanır.
3. **Botun Devreye Girmesi:** `buy_me_a_coffee_uploader.py` çalıştırıldığında bot Chrome tarayıcıyı açar ve sisteme giriş yapar.
4. **Otomatik Yükleme (Upload):** Bot, CSV'deki sıraya göre "New Extra" (Yeni Ürün) sayfasına girer; ilgili klasörün içindeki ham duvar kağıtlarını geçici (Temp) bir ZIP'e koyarak bunu indirilebilir dosya (File) olarak siteye yükler. Ayrıca Kapak fotoğrafını da seçer.
5. **Onay ve Yayın:** Tüm başlıklar, fiyatlar ve açıklamalar otomatik doldurulunca bot beklemeye geçer. Kullanıcı ekrandan her şeyin doğru olduğunu görüp kendi eliyle "Yayınla"ya basar ve terminale dönüp "Enter" diyerek botu bir sonraki klasöre yollar.
