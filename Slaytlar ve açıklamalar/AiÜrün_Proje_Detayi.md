# AiÜrün: AI Destekli Profesyonel Reklam Görseli Oluşturma Sistemi

## 📌 Proje Özeti
Bu proje, kullanıcıların sıradan ürün fotoğraflarını yükleyerek yapay zeka desteğiyle profesyonel, stüdyo kalitesinde reklam görsellerine dönüştürmelerini sağlayan tam kapsamlı bir web uygulamasıdır. Sistem; Next.js tabanlı modern bir arayüz, Supabase destekli veritabanı, n8n otomasyonu, Google Gemini ve OpenAI DALL-E 3 yapay zeka modellerinin entegrasyonuyla çalışır.

## 🚀 Temel Özellikler
- **Otomatik Görsel Analizi:** Yüklenen ürün resmi Google Gemini 2.0 tarafından analiz edilir, ürün özellikleri belirlenir ve yeni görsel için en uygun prompt (komut) otomatik oluşturulur.
- **Yüksek Kaliteli Görsel Üretimi:** OpenAI DALL-E 3 kullanılarak ürüne özel, yüksek çözünürlüklü (1024x1024) profesyonel reklam görselleri oluşturulur.
- **Modern Web Arayüzü:** Next.js 14 ve Tailwind CSS ile geliştirilmiş, Vercel üzerinde hızlı çalışan kullanıcı dostu ön yüz.
- **Tam Otomasyon Akışı (n8n):** Supabase'e resim yüklendiğinde tetiklenen webhook ile; analiz, prompt oluşturma, görsel üretme ve veritabanına kaydetme süreçleri n8n üzerinden el değmeden gerçekleşir.
- **Bulut Veri Yönetimi:** Ürünlerin orijinal resimleri, yapay zekanın ürettiği yeni görseller ve veri tabanı kayıtları Supabase üzerinde saklanır.

## 🛠️ Kullanılan Teknolojiler
- **Frontend (Kullanıcı Arayüzü):** React, Next.js 14, Tailwind CSS
- **Backend & Storage:** Supabase (PostgreSQL, Storage, REST API, Webhook)
- **Otomasyon Motoru:** n8n 
- **Yapay Zeka Modelleri:**
  - Google Gemini 2.0 (Görsel analiz ve prompt mühendisliği için)
  - OpenAI DALL-E 3 (Reklam görseli üretimi için)

## 📁 Proje Mimarisi ve Dosya Yapısı
- `sertselo-ai-ads/`: Next.js web uygulamasının bulunduğu ana dizin.
  - `src/components/`: Yükleme formu (`UploadForm`), görsel galeri (`ImageGallery`) gibi React bileşenleri.
  - `src/lib/`: Supabase bağlantı istemcisi ve ayarları.
- `n8n_workflow.json`: n8n otomasyon pipeline'ının içe aktarılabilir (import) şablon dosyası.
- `supabase_setup.sql`: Supabase'de gerekli tabloları, yetkilendirmeleri ve storage bucket ayarlarını yapılandıran SQL kurulum betiği.
- Dokümantasyonlar: `project-overview-modern.md`, `complete-code-guide.md` ve adım adım kurulum rehberleri projede detaylıca yer alır.

## ⚙️ Nasıl Çalışır? (Sistem Akışı)
1. **Veri Girişi:** Kullanıcı web arayüzünden ürün resmini yükler.
2. **Kayıt ve Tetikleme:** Resim Supabase'e kaydedilir. Bu kayıt bir Webhook'u tetikleyerek sinyali n8n'e gönderir.
3. **AI Analizi:** n8n, resmi Supabase'den çekip Google Gemini'ye gönderir. Gemini resme bakarak detaylı bir reklam görseli oluşturma promptu yazar.
4. **Görsel Üretimi:** n8n, bu promptu OpenAI DALL-E 3'e iletir ve yeni profesyonel reklam görseli oluşturulur.
5. **Geri Bildirim:** Üretilen görsel n8n tarafından tekrar Supabase'e yüklenir ve web arayüzünde kullanıcıya sergilenir.
