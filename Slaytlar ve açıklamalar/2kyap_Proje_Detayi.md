# 2kyap Projesi: AI Image Upscaler (Yapay Zeka Destekli Görüntü Büyütme)

## 📌 Proje Özeti
Bu proje, düşük çözünürlüklü görüntüleri yapay zeka kullanarak 4 katına (4x) kadar kaliteden ödün vermeden büyüten ve detaylandıran masaüstü tabanlı bir uygulamadır. Görüntü işleme motoru olarak **RealESRGAN** ve yüz iyileştirme işlemleri için **GFPGAN** modellerini kullanır. Arayüzü modern ve kullanıcı dostu olması adına `customtkinter` ile geliştirilmiştir.

## 🚀 Temel Özellikler
- **Tekli ve Çoklu (Batch) İşleme:** Sadece tek bir fotoğrafı değil, bir klasör içerisindeki tüm fotoğrafları toplu olarak büyütebilme.
- **Yapay Zeka Modelleri:** 
  - `RealESRGAN_x4plus`: Genel amaçlı, gerçek hayat fotoğraflarını büyütmek için.
  - `RealESRGAN_x4plus_anime_6B`: Anime, illüstrasyon ve çizim tarzı görüntüler için özel optimize edilmiş model.
- **Yüz İyileştirme (Face Enhancement):** GFPGAN entegrasyonu sayesinde fotoğraflardaki bozulmuş veya bulanık yüzleri otomatik tespit edip netleştirme ve onarma.
- **Gelişmiş GPU Desteği:** Sistemdeki CUDA destekli ekran kartını otomatik olarak algılar ve tüm yapay zeka işlemlerini işlemci (CPU) yerine çok daha hızlı olan ekran kartı (GPU) üzerinde gerçekleştirir.
- **Geliştirici Seçenekleri (Dev Options):**
  - **Tile Size & Padding:** Düşük VRAM'e (video belleği) sahip ekran kartlarında "Out of Memory" (Bellek Yetersiz) hatalarını önlemek için büyük görüntüleri kare (tile) parçalara bölerek işleme yeteneği.
  - **FP16 Modu (Half Precision):** İşlem hızını ciddi oranda artıran ve bellek kullanımını düşüren yarı hassasiyet modu.

## 🛠️ Kullanılan Teknolojiler ve Kütüphaneler
- **Arayüz (GUI):** `customtkinter` (Modern, Windows stili ile uyumlu arayüz)
- **Görüntü İşleme:** `opencv-python` (cv2), `Pillow`, `numpy`
- **Yapay Zeka / Derin Öğrenme:** `torch` (PyTorch), `torchvision`, `realesrgan`, `gfpgan`, `basicsr`

## 📁 Proje Dosya Yapısı
- `main.py`: Uygulamanın ana dosyası. Arayüz bileşenlerini, butonları, sekmeleri ve kullanıcı etkileşimlerini içerir.
- `upscaler.py`: RealESRGAN ve GFPGAN modellerinin yüklendiği, donanımın seçildiği ve görüntü çözünürlüğünü artırma işlemlerinin yürütüldüğü arka plan (backend) dosyası.
- `run.bat`: Uygulamayı başlatmak için kullanılan Windows toplu iş dosyası. Başlangıçta bağımlılıkları da kontrol eder.
- `setup.py` & `requirements.txt`: Projenin ihtiyaç duyduğu dış kütüphanelerin listesi ve kurulum dosyaları.

## ⚙️ Nasıl Çalışır?
1. Kullanıcı `run.bat` dosyasını çalıştırarak uygulamayı açar.
2. Basit arayüz üzerinden işlem yapılacak fotoğraf veya fotoğrafların bulunduğu klasör seçilir.
3. Kullanılacak AI modeli seçilir ve isteğe bağlı olarak "Face Enhancement" (Yüz İyileştirme) aktif edilir.
4. Gerekirse "Dev Options" menüsünden GPU bellek kullanımına göre optimizasyon ayarları yapılır.
5. "START UPSCALE" butonuna basılır ve fotoğraf/fotoğraflar 4 kat daha büyük, net ve kaliteli olarak belirlenen klasöre kaydedilir.
