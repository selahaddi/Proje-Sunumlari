# Davetiye: Çok Kiracılı (Multi-Tenant) Dijital Düğün Davetiye Platformu

## 📌 Proje Özeti
Davetiye; Next.js (App Router), React, Tailwind CSS ve Supabase kullanılarak geliştirilmiş, **çok kiracılı (multi-tenant) ve dinamik URL yönlendirmeli** bir dijital düğün davetiye platformudur. Her çift için ayrı ayrı web uygulaması kurmak yerine, tek bir merkezi altyapı üzerinden alt alan adları (`ayse-ahmet.domain.com`) veya URL yolları (`domain.com/ayse-ahmet`) aracılığıyla **7 özgün tasarım teması** ve **3 kademeli özellik paketi** (toplam 28 şablon) dinamik olarak sunulur.

## 🚀 Temel Özellikler
- **Çok Kiracılı Dinamik Yönlendirme (`middleware.js`):** Gelen isteklerdeki alt alan adını veya URL yolunu analiz ederek Supabase `couples` tablosunu sorgular; aktif bir çift kaydı eşleştiğinde tarayıcı adres çubuğundaki URL'yi değiştirmeden (`NextResponse.rewrite`) ilgili şablonu (`/{template_id}/code.html`) arka planda sunar.
- **7 Özgün Tasarım Teması × 4 Varyant (28 Hazır Şablon):** `Earth & Air` (1), `Minimalist Editorial` (2), `Coastal Serenity` (3), `Neo-Urban Kinetic` (4), `Terracotta & Olive` (5), `Midnight & Gild` (6) ve `Bohemian Rhapsody` (7) tasarım dillerinin her biri için Standart, Başlangıç, Orta ve İleri (Premium) sürümleri.
- **3 Kademeli Modüler Özellik Paketleri (`components/`):**
  - **Başlangıç (`components/baslangic/`):** Çift hikâyesi ve galeri, düğün program akışı, Google Takvim & `.ics` Apple Takvim ekleme (`CalendarAdd.jsx`), Google/Apple/Yandex Harita navigasyonu (`MapNavigation.jsx`).
  - **Orta (`components/orta/`):** Supabase bağlantılı canlı **Katılım Formu / LCV** (`RsvpForm.jsx` / `LcvForm.jsx` → `rsvp_responses`), **WhatsApp** üzerinden konum hatırlatıcısı ve hızlı mesajlaşma (`WhatsappNotify.jsx`), **Spotify Şarkı İsteği** (`SpotifyRequest.jsx` → `song_requests`).
  - **İleri / Premium (`components/ileri/`):** Misafirlerin QR kod veya doğrudan yükleme ile anı paylaştığı **Canlı Fotoğraf Duvarı** (`PhotoWall.jsx`), filigransız yüksek çözünürlüklü indirme/satın alma akışlı **Premium Stüdyo Galerisi** (`PremiumGallery.jsx` → `photo_purchases`), tek tıkla IBAN kopyalama, rezerve edilebilir ihtiyaç listesi ve tebrik mesajı içeren **Dijital Takı & Hediye Listesi** (`GiftList.jsx`).
- **Şifre Korumalı Yönetici Paneli (`app/page.jsx`):** Yetkili kullanıcının yeni çiftler için URL uzantısı tanımladığı (Türkçe karakterleri otomatik ASCII'ye dönüştüren regex ile `ğ→g`, `ş→s` vb.), 28 şablon-paket kombinasyonundan seçim yapıp tek tıkla Supabase veritabanına kaydederek yayına aldığı yönetim ekranı.
- **Hızlı Dağıtım Betikleri (`github_guncelle.bat`, `github_guncelle.sh`):** Yeni eklenen şablon ve tasarım güncellemelerini tek komutla GitHub ve Vercel üzerine aktaran yayınlama betikleri.

## 🛠️ Kullanılan Teknolojiler
- **Frontend & Framework:** Next.js (App Router), React, Tailwind CSS, Material Symbols
- **Yönlendirme Katmanı:** Next.js Edge Middleware (`NextResponse.rewrite`)
- **Veritabanı & Depolama:** Supabase PostgreSQL (`couples`, `rsvp_responses`, `song_requests`, `photo_purchases` tabloları) ve Supabase Storage
- **Barındırma & Otomasyon:** Vercel (Wildcard Subdomain & Path Hosting), GitHub Otomatik Dağıtım Scriptleri

## 📁 Proje Mimari Yapısı
- `middleware.js`: Gelen host ve URL yolunu çözümleyen, Supabase `couples` sorgusuna göre şablonu URL değiştirmeden sunan dinamik yönlendirici.
- `app/page.jsx` & `app/layout.jsx`: Şifre korumalı admin girişi, Türkçe karakter temizleyici URL oluşturucu ve 28 şablon-paket atama arayüzü.
- `components/`: `baslangic/` (`CalendarAdd`, `MapNavigation`), `orta/` (`LcvForm`, `RsvpForm`, `SpotifyRequest`, `WhatsappNotify`), `ileri/` (`PhotoWall`, `PremiumGallery`, `GiftList`) modüler React bileşenleri.
- `public/`: `1`–`7` arası temalar ile `_baslangic`, `_orta`, `_ileri` paket varyantlarına ait statik HTML (`code.html`) ve tasarım dosyaları (`DESIGN.md`, galeri görselleri).
- `github_guncelle.bat` & `github_guncelle.sh`: Tek tıkla GitHub/Vercel senkronizasyon betikleri.

## ⚙️ Nasıl Çalışır? (Sistem Akışı)
1. **Yönetici Ataması:** Yönetici `/` paneline giriş yapar, çift için özel URL adını (ör. `ayse-ahmet`) ve seçilen tema + paket kombinasyonunu (ör. `2_orta` veya `1_ileri`) belirler.
2. **Veritabanı Kaydı:** Kayıt işlemiyle çiftin `subdomain` ve `template_id` bilgisi Supabase'deki `couples` tablosuna yazılır.
3. **Dinamik Ziyaretçi Yakalama:** Davetli `ayse-ahmet` adresini ziyaret ettiğinde `middleware.js` isteği yakalar ve Supabase'den aktif şablon kimliğini doğrular.
4. **Şeffaf Sunum ve Canlı Etkileşim:** Middleware tarayıcı adresini değiştirmeden ilgili `code.html` şablonunu render eder; misafirler seçilen pakete göre LCV yanıtı, şarkı isteği, fotoğraf paylaşımı ve dijital tebrik işlemlerini doğrudan Supabase üzerinde gerçekleştirir.
