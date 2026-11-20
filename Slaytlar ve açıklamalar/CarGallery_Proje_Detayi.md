# CarGallery (Dortmund Fleet Finance): Dijital Showroom ve Otomatik Finansman Platformu

## 📌 Proje Özeti
CarGallery (Dortmund Fleet Finance), lüks araç envanterini sinematik bir kullanıcı deneyimiyle sergileyen, anlık finansman hesaplamaları sunan ve müşteri teklif taleplerini otomatik olarak 300 DPI kurumsal PDF belgesine dönüştürüp e-posta ile ileten tam kapsamlı (Full-Stack) bir **Dijital Showroom ve Filo Finansman Platformu**dur. React (Vite), Tailwind CSS ve Framer Motion ile geliştirilen ön yüzü; Express + SQLite / Supabase hibrit veri katmanı, Vercel Serverless fonksiyonları ve n8n + Python (Flask & Pillow) otomasyon motoruyla bütünleşik çalışır.

## 🚀 Temel Özellikler
- **Sinematik Scroll Video Hero (`ScrollVideoTest.jsx`):** 277 yüksek çözünürlüklü showroom karesini kullanıcının sayfa kaydırma (scroll) hareketine bağlı olarak akıcı biçimde oynatan, kademeli ön yükleme (progressive batch loading) destekli etkileşimli vitrin deneyimi.
- **Dijital Showroom & Gelişmiş Filtreleme (`Home.jsx`):** Kategori bazlı filtreleme (`SUV`, `Sedan`, `Electric`, `Performance`), başlık/özet/etiket araması, tarih ve alfabetik sıralama ile Glassmorphism tasarım dilinde araç vitrini.
- **Canlı Finansman Hesaplayıcı & Lightbox Galeri (`ContentDetail.jsx`):** Peşinat kaydırıcısı (slider) ve 12–84 ay vade seçenekleriyle aylık taksit, toplam faiz ve toplam geri ödeme tutarını anlık hesaplama; yakınlaştırma (zoom) ve sürükleme (pan) destekli çoklu görsel Lightbox galeri; `react-helmet-async` ile dinamik SEO ve Open Graph meta etiketleri.
- **3 Dilde Yerelleştirme (`LanguageContext.jsx`, `translations.js`):** Türkçe (`TR`), İngilizce (`EN`) ve Almanca (`DE`) arasında anlık dil geçişi ve dile duyarlı para/sayı biçimlendirmesi.
- **Tam Kapsamlı Yönetim Paneli (`Dashboard.jsx`):** Yetkilendirme korumalı admin panelinde araç ekleme/düzenleme/silme (CRUD), `@dnd-kit` ile sürükle-bırak vitrin sıralaması (`sort_order`), çoklu görsel yükleme, canlı filo portföy değeri istatistikleri ve SSE / Supabase Realtime üzerinden anlık gelen teklif bildirimleri.
- **Hibrit Bulut & Yerel Mimari (`src/supabaseClient.js`, `server/index.js`, `api/`):** Mevcut frontend kodunu bozmadan yerel Express 5 + SQLite (`better-sqlite3`) API'sine bağlanan Supabase İstemci Emülatörü, Vercel Serverless API uç noktaları (`api/contents.js`, `api/generate-offer.js`) ve `yedekler/contents.json` yedek fallback katmanı.
- **Otomatik PDF Teklif & n8n İş Akışları (`scripts/api_server.py`, `Profiauto - Generate PDF via API.json`, `N8N_workflow.json`):** Müşteri teklif formunu gönderdiğinde hem Vercel Serverless (`PDFKit` + `Nodemailer`) hem de n8n Webhook → Python Flask & Pillow (300 DPI A4 kurumsal PDF üretimi) → Gmail akışı üzerinden kişisel finansman teklifi PDF'i hazırlanıp müşteriye e-postalanır; n8n üzerinden dış sistemlerden gelen araç verileri de otomatik olarak `contents` tablosuna aktarılabilir.
- **Statik Sayfa Üretici (`scripts/generate_static_pages.js`):** Veritabanındaki araç envanterinden bağımsız statik HTML vitrin ve detay sayfaları derleyen yardımcı betik.

## 🛠️ Kullanılan Teknolojiler
- **Frontend (Kullanıcı Arayüzü):** React 19, Vite, Tailwind CSS, Framer Motion, React Router DOM v7, `@dnd-kit`, Lucide React, `react-helmet-async`
- **Backend & Veritabanı:** Express 5, SQLite (`better-sqlite3`), Supabase (`@supabase/supabase-js`), JWT, `bcryptjs`, Multer, Server-Sent Events (SSE)
- **Otomasyon & PDF Motoru:** n8n (Webhook & Workflow Otomasyonu), Python Flask & Pillow (`300 DPI A4 PDF`), PDFKit, Nodemailer (Gmail / SMTP), Vercel Serverless Functions

## 📁 Proje Mimari Yapısı
- `src/pages/`: `Home.jsx` (Vitrin), `ContentDetail.jsx` (Finansman Hesaplayıcı & Lightbox), `Dashboard.jsx` (Yönetim Paneli), `Services.jsx` (Hizmetler & Süreç), `Login.jsx` (Admin Girişi).
- `src/components/`: `ScrollVideoTest.jsx` (277 Kare Scroll Video), `ContentCard.jsx`, `DashboardRow.jsx`, `Navbar.jsx`, `SideNavBar.jsx`, `Footer.jsx`.
- `src/supabaseClient.js`: Yerel SQLite API'si, Realtime SSE akışı ve JSON fallback desteği sunan hibrit Supabase emülatörü.
- `server/`: `index.js`, `db.js`, `seed.js` (Express REST API, JWT doğrulama, Multer medya yükleme ve SQLite veritabanı).
- `api/`: `contents.js` ve `generate-offer.js` (Vercel Serverless PDFKit + Nodemailer teklif uç noktaları).
- `scripts/`: `api_server.py`, `generate_pdf.py` (Pillow tabanlı 300 DPI A4 PDF sunucusu), `generate_static_pages.js`.
- `N8N_workflow.json` & `Profiauto - Generate PDF via API.json`: İçe aktarılabilir n8n otomasyon şablonları.

## ⚙️ Nasıl Çalışır? (Sistem Akışı)
1. **Vitrin ve Keşif:** Ziyaretçi ana sayfada 277 karelik scroll video deneyimini izler, kategori/arama/sıralama filtreleriyle araçları inceler.
2. **Finansman Yapılandırma:** Araç detay sayfasında peşinat ve 12–84 ay arası vade seçerek aylık taksit, toplam faiz ve toplam maliyeti canlı olarak hesaplar.
3. **Teklif Talebi:** "Teklif İste" modalını doldurup gönderdiğinde `/api/generate-offer` (veya n8n webhook) tetiklenir; talep `offers` tablosuna kaydedilir.
4. **Otomatik PDF ve E-Posta:** Arka planda Python Flask + Pillow veya PDFKit motoru müşteri ve araç bilgilerini içeren kurumsal PDF teklifini üretir ve Nodemailer/Gmail üzerinden müşteriye gönderir.
5. **Canlı Panel Takibi:** Yönetici Dashboard'da gelen yeni teklifi SSE/Realtime bildirimiyle anında görür, sürükle-bırak ile vitrin sırasını ve envanteri yönetir.
