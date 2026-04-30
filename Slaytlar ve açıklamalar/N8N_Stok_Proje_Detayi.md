# N8N Stok: Süpermarket Stok Analiz Otomasyonu

## 📌 Proje Özeti
Bu proje, perakende işletmeleri ve süpermarketler için tasarlanmış yapay zeka destekli bir stok analiz otomasyonudur. N8n üzerinden kurulan bu sistem; buluta (Google Drive) yüklenen güncel stok verilerini otomatik olarak okur, verileri parçalara bölerek (batch processing) yapay zekaya (OpenAI) analiz ettirir ve "Hangi üründen kaç adet sipariş edilmeli?" sorusunun cevabını içeren yepyeni bir Excel raporu üreterek ilgili klasöre kaydeder.

## 🚀 Temel Özellikler
- **Tam Otomatik Tetiklenme:** Google Drive'daki `Girdi` klasörüne yeni bir stok Excel dosyası eklendiğinde (Trigger) süreç el değmeden otomatik başlar.
- **Toplu Veri İşleme (Batching/Loop):** Büyük veri setlerinde AI sınırlarına (Token Limitleri) takılmamak ve kaliteyi korumak için, stok listesini 10'arlı gruplara (Loop) bölerek işleme stratejisi.
- **Akıllı Stok Analizi:** OpenAI API (GPT-4o / GPT-4o-mini) sayesinde sadece mevcut stoka bakılmaz; satış hızı, kritik stok eşikleri ve geçmiş veriler harmanlanarak en mantıklı satın alma önerisi hesaplanır.
- **Otomatik Excel Çıktısı:** Dağınık veriler AI analizinden geçtikten sonra, mağaza müdürünün hemen kullanabileceği formatta temiz bir Excel raporuna (`Siparis_Onerileri_[Tarih].xlsx`) dönüştürülüp `Cikti` klasörüne aktarılır.
- **Düşük Maliyet:** Akıllı döngü sistemi ve ucuz modellerin (gpt-4o-mini) optimizasyonu sayesinde, yüksek miktarda ürün analizi aylık sadece 1-2$ gibi çok düşük maliyetlerle yapılabilir.

## 🛠️ Kullanılan Teknolojiler
- **Otomasyon Motoru:** n8n
- **Bulut Depolama ve Tetikleyici:** Google Drive API (OAuth2 Entegrasyonu)
- **Veri Biçimlendirme:** N8N Spreadsheet File Node'ları (Excel okuma/yazma) ve JavaScript (AI dönüşlerini JSON objesine parse etmek için)
- **Yapay Zeka:** OpenAI API
- **Test Aracı:** Python (Sistemi test etmek için rastgele veri üreten `create_sample_data.py` betiği)

## 📁 Proje Klasör Yapısı
- `stok_analiz_workflow.json` (ve `_2`, `_3` versiyonları): N8n'e saniyeler içinde "Import" edilip hemen çalıştırılabilecek olan tüm bağlantıları içeren iş akışı şablonları.
- `KURULUM_REHBERI.md`: Google Drive API key alma, n8n üzerinde kimlik (Credential) doğrulama ve dosyaların nasıl yapılandırılacağını adım adım anlatan rehber.
- `create_sample_data.py`: Sistemi gerçek veriler olmadan test edebilmek için 50 satırlık, tutarlı "dummy" (sahte) süpermarket ürünleri ve satış rakamları üreten Python kodu.
- `n8n_stock_analysis_workflow_logic.md`: Projenin mimarisini, "neden döngü (loop) kullanıldığı"nı ve AI Prompt'larının arkasındaki mühendisliği açıklayan tasarım belgesi.
- `Veriler/` & `stok_verileri.xlsx`: Çalışma sırasında kullanılan örnek girdi ve çıktılar.

## ⚙️ Sistem Akışı (Nasıl Çalışır?)
1. **Veri Yükleme:** İşletme veya sistem, güncel mağaza stoklarını barındıran Excel dosyasını Google Drive'daki `Girdi` klasörüne atar.
2. **N8N Harekete Geçer:** N8n'deki "Google Drive Trigger" nodu durumu fark eder, Excel'i sunucuya indirip içindeki satırları dijital listeye (JSON Array) dönüştürür.
3. **AI Analizi:** Listedeki ürünler 10'lu paketler halinde döngüye sokulur. OpenAI her bir paket için; stok sayısını, son bir aylık satış hızını değerlendirir ve alınması gereken ürün miktarlarını belirler.
4. **Veri Birleştirme:** Çıkan analiz metinleri "Code" nodu sayesinde temiz bir JSON dizisine çevrilir ve tüm paketler tek bir listede birleşir.
5. **Raporlama:** Birleşen JSON listesinden yeni bir Excel dosyası basılır ve Google Drive'daki `Cikti` klasörüne "Sipariş Önerileri" adıyla kaydedilir. İşlem başarıyla sonlanır.
