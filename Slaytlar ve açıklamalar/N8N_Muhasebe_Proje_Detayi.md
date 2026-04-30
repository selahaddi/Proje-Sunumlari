# N8N Muhasebe: Fatura ve Gider Otomasyonu (OCR)

## 📌 Proje Özeti
Bu proje, işletmelerin ve mali müşavirlerin fatura giriş süreçlerini tamamen otomatize etmek için tasarlanmış akıllı bir muhasebe çözümüdür. E-posta yoluyla gelen fatura dosyalarını (PDF, görsel vb.) yakalar, OCR (Optik Karakter Tanıma) ve yapay zeka (LLM) kullanarak içeriğini okur ve anlamlandırılmış verileri anında Google Sheets gibi tablolara kaydeder.

## 🚀 Temel Özellikler
- **E-Posta Yakalama:** Özel fatura e-posta adresine düşen mailleri saniyeler içinde otomatik olarak tespit etme (Gmail / IMAP entegrasyonu).
- **OCR ile Belge Okuma:** Gelen e-posta eklerindeki PDF veya resim (JPEG/PNG) formatındaki faturaları dijital metne dönüştürme (PDF4me vb. servisler ile).
- **Yapay Zeka Destekli Veri Ayıklama:** OpenAI (ChatGPT) veya Google Gemini kullanarak faturadaki karmaşık metinleri analiz etme. Fatura Numarası, Tarih, Vergi Dairesi, KDV, Matrah ve Toplam Tutar gibi spesifik bilgileri hatasız ayıklama.
- **Otomatik Raporlama ve Kayıt:** Ayıklanan verileri doğrudan Google Sheets'e veya API destekli herhangi bir ERP/Muhasebe yazılımına yeni bir kayıt (satır) olarak ekleme.
- **Ticari Ölçeklenebilirlik:** SaaS (Aylık Abonelik), Anahtar Teslim Kurulum veya Dijital Şablon (Template) satışı olarak piyasaya sunulabilecek ticari altyapı.

## 🛠️ Kullanılan Teknolojiler
- **Otomasyon Platformu:** n8n 
- **OCR ve Dosya İşleme:** PDF4me API, n8n yerleşik PDF okuma araçları
- **Yapay Zeka (LLM):** OpenAI API veya Google Gemini API (Veri anlamlandırma için)
- **Veritabanı / Çıktı:** Google Sheets, Google Drive
- **Sunucu & Altyapı:** Docker (VPS üzerinde bağımsız barındırma için)

## 📁 Proje Dosya Yapısı
- `workflows/`: E-posta dinleme, OCR ile metin çıkarma, AI ile veri yapılandırma ve Google Sheets kayıt işlemlerini barındıran içe aktarılabilir n8n JSON dosyaları.
- `YedekFaturalar/`: İş akışının (workflow) test edilmesi ve yapay zekanın doğruluğunun ölçülmesi için kullanılan örnek fatura şablonları/pdf'leri.
- `rehber_satis_ve_kurulum.md`: Projenin nasıl paraya dönüştürüleceğini, sunucu kurulum aşamalarını, potansiyel müşterilere ROI (Yatırım Getirisi) hesaplamasının nasıl sunulacağını ve örnek fiyatlandırma tablolarını içeren ticari strateji dokümanı.

## ⚙️ Nasıl Çalışır? (Sistem Akışı)
1. **Tetikleyici (Trigger):** Bir tedarikçi veya müşteri, sisteme tanımlı e-posta adresine fatura gönderir.
2. **Ekstraksiyon:** n8n e-postadaki eki (PDF) alır ve OCR servisine iletir.
3. **Anlamlandırma:** OCR'dan dönen düz metin, AI modeline (Örn: ChatGPT) özel bir "Sistem Komutu" (Prompt) ile gönderilir. Yapay zeka faturadaki satır kalemlerini, vergileri ve toplam tutarları ayırarak temiz bir JSON objesine dönüştürür.
4. **Veri Girişi:** Elde edilen temiz JSON verisi Google Sheets'teki ilgili sütunlara otomatik olarak yazılır ve manuel veri girişine gerek kalmaz.
