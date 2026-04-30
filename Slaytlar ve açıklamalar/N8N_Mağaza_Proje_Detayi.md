# N8N Mağaza: Kişiselleştirilmiş Satış Hunisi Optimizasyon Ajanı

## 📌 Proje Özeti
Bu proje, e-ticaret siteleri için geliştirilmiş, n8n (otomasyon platformu) üzerinde çalışan yapay zeka destekli bir satış ve pazarlama aracıdır. Sistem, müşterilerin e-ticaret sitesindeki davranışlarını (özellikle sepette bırakılan ürünler ve gezilen kategoriler) analiz ederek, onları satın almaya ikna edecek "hiper-kişiselleştirilmiş" e-posta içerikleri üretir.

## 🚀 Temel Özellikler
- **Satış Hunisi Tespiti:** Müşterinin sepet bırakma veya gezinme durumuna göre satın alma döngüsünün hangi aşamasında (Karar, İlgi vb.) olduğunu otomatik olarak belirler.
- **Terk Edilmiş Sepet (Abandoned Cart) Hatırlatıcısı:** Sepette unutulan ürünler için yüksek dönüşüm getiren hatırlatma içerikleri yazar.
- **Stratejik Ürün Tavsiyesi (Cross-Sell):** Sadece sepetteki ürünleri listelemez; bütçe segmentine ve son gezilen kategoriye uygun, kâr marjı yüksek veya stok fazlası olan 2 tamamlayıcı ürünü stratejik olarak önerir.
- **Profesyonel "Dijital Asistan" Personası:** Metinler soğuk bir şablon gibi değil, kullanıcıya ismiyle hitap eden, çözüm odaklı, samimi bir asistan ağzıyla yazılır.
- **Psikolojik Satış Taktikleri:** Hazırlanan içeriklerde aciliyet yaratacak unsurlar (ör. stok azalması) ve tıklamayı artıracak güçlü "Harekete Geçirici Mesaj" (Call to Action - CTA) buton metinleri bulunur.

## 🛠️ Kullanılan Teknolojiler
- **Otomasyon Motoru:** n8n 
- **Yapay Zeka ve Zincirleme (Orchestration):** LangChain (n8n içerisindeki özel LangChain düğümleri)
- **Dil Modeli (LLM):** DeepSeek Chat Model (AI analizi ve içerik üretimi için)
- **Veri Ayrıştırma:** Structured Output Parser (AI'dan gelen uzun metinleri, sistemin kullanabileceği temiz JSON yapılarına çevirmek için)
- **JavaScript:** Özel veri şekillendirmeleri ve JSON parsing işlemleri.

## 📁 Proje Dosya Yapısı
- `sales-funnel-agent.json`: n8n platformuna aktarıldığında (import) anında çalışmaya hazır olan otomasyon iş akışı dosyası. Yapay zeka promptları, düğüm bağlantıları ve API yapılandırmaları bu dosyanın içindedir.
- `N8N_Market.pdf`: Sistemin teorik altyapısını, e-ticaret pazar yeri kurgusunu ve satış hunisi mantığını görsellerle detaylandıran sunum/dokümantasyon dosyası.

## ⚙️ Nasıl Çalışır? (Sistem Akışı)
1. **Veri Yakalama:** E-ticaret platformundan webhook aracılığıyla müşteri verisi (isim, bütçe, son incelenenler, sepetteki ürünler) n8n'e gelir. (Şu anda workflow içinde Mock/Test düğümü ile simüle edilmektedir).
2. **Yapay Zeka Görevlendirmesi:** Gelen veriler, LangChain üzerinden "Satış E-postası Üretici" düğümüne gönderilir. Prompt içerisinde AI'ya kurallar (stok durumunu gözet, CTA ekle, aciliyet yarat) iletilir.
3. **Yapısal Veri Üretimi:** DeepSeek modeli bu analizleri yaparak Structured Output Parser yardımıyla standart bir metin yerine parçalanmış bir JSON verisi üretir (Örn: Sadece konu satırı, giriş cümlesi, buton linki ayrı ayrı).
4. **Çıktı Kontrolü:** Son "Code" düğümü, verinin doğru bir JSON olduğundan emin olur ve bu temiz veriyi CRM veya e-posta gönderim platformlarına (Mailchimp vb.) aktarılmak üzere hazır hale getirir.
