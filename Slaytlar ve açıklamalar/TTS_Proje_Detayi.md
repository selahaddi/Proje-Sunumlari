# TTS: Piper TTS Ses Oluşturucu (Text-to-Speech)

## 📌 Proje Özeti
Bu proje, yazılı metinleri (Text) yüksek kaliteli insan sesine (Speech) dönüştüren yerel bir masaüstü uygulamasıdır. Arka planda açık kaynaklı, hızlı ve düşük donanım gereksinimli **Piper TTS** motorunu kullanır. Modern ve kullanıcı dostu arayüzü sayesinde herkesin bilgisayarında, internet bağlantısına ihtiyaç duymadan (API maliyeti olmadan) profesyonel seslendirmeler yapabilmesini sağlar.

## 🚀 Temel Özellikler
- **Tamamen Yerel (Offline) İşlem:** Ses oluşturma süreci buluta veri göndermeden tamamen kendi bilgisayarınızın işlemcisiyle yapılır. Veri gizliliği sağlar.
- **Dahili Model İndirici (Model Downloader):** Uygulama içindeki menüden, dışarıdan bulduğunuz farklı ses modellerinin (ONNX formatında) URL'lerini girerek sisteme tek tıkla yeni insan sesleri ekleyebilirsiniz.
- **Asenkron Çalışma:** Ses oluşturma ve model indirme işlemleri arka planda (`threading`) çalışır; bu sayede uzun metinler okunurken bile uygulama donmaz veya çökmez.
- **Hızlı Dinleme:** Oluşturulan `.wav` dosyaları, işlem biter bitmez "Ses Oynat" butonuyla doğrudan uygulama üzerinden dinlenebilir.
- **Modern ve Şık Arayüz:** `customtkinter` kütüphanesiyle hazırlanan, Dark/Light/System tema destekli arayüz.

## 🛠️ Kullanılan Teknolojiler
- **Kullanıcı Arayüzü (GUI):** Python `customtkinter`, `tkinter`
- **Yapay Zeka Ses Motoru:** Piper TTS (`piper-tts` CLI)
- **Sistem İletişimi:** `subprocess` (Piper'ı arka planda çalıştırmak için), `threading`
- **Dosya ve Medya:** `requests` (İnternetten model çekmek için), `winsound` (Windows üzerinde ses oynatmak için)

## 📁 Proje Dosya Yapısı
- `app.py`: Ana masaüstü uygulamasıdır. Tüm arayüz tasarımı, buton işlevleri, Piper ile iletişim ve model indirme mantığı bu kodun içindedir.
- `models/`: Piper TTS'in anlayabileceği `.onnx` model dosyalarının ve `.json` konfigürasyonlarının depolandığı klasör. Uygulama açılırken buradaki sesleri tarar.
- `download_models.py` / `find_models.py`: Arayüz olmadan komut satırından alternatif model arama ve indirme betikleri.
- `*.wav` / `*.mp3`: Önceden oluşturulmuş, uygulamanın çıktısı olan örnek seslendirme dosyaları (Örn: `atlas1.wav`, `outputEmel.mp3`).

## ⚙️ Nasıl Çalışır? (Sistem Akışı)
1. **Ses (Model) Seçimi:** Uygulama açıldığında `models` klasörünü tarar. Kullanıcı listeden okumayı yapacak sesi seçer. (Eğer ses yoksa uygulama içinden indirebilir).
2. **Veri Girişi:** Sol menüdeki metin kutusuna okunacak Türkçe veya yabancı dildeki metin girilir.
3. **Tetikleme ve İletişim:** "Ses Oluştur" butonuna tıklandığında Python, kullanıcının metnini alır ve `subprocess` kütüphanesi aracılığıyla Piper TTS motoruna "Bunu seçili ONNX modeliyle oku ve WAV dosyasına kaydet" komutunu gönderir.
4. **Çıktı:** Piper motoru işlemi bitirince, arayüze "Tamamlandı" bilgisini iletir ve kaydedilen dosya hazır hale gelir.
5. **Kontrol:** Oynatma butonu aktifleşir ve kullanıcı oluşturduğu sesi anında test eder.
