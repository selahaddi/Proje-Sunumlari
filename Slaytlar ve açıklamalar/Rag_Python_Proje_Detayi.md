# Rag Python: Esnek Kurumsal RAG (Retrieval-Augmented Generation) Sistemi

## 📌 Proje Özeti
Bu proje, her türlü şirket ortamına ve farklı kurumsal departman ihtiyaçlarına (İK, Hukuk, Teknik Destek, Yönetim) anında uyarlanabilen esnek bir RAG altyapısıdır. Şirketlere ait özel dokümanların (kılavuzlar, pdf'ler) güvenli bir şekilde okunarak vektörel veritabanlarına kaydedilmesini ve ardından n8n üzerinden yönetilen yapay zeka ajanlarının bu verileri referans alarak halüsinasyonsuz, kuruma özel ve %100 doğru cevaplar üretmesini sağlar.

## 🚀 Temel Özellikler
- **Kesintisiz Veri Yükleme (Ingestion):** Yüksek hacimli şirket belgeleri yüklenirken API sınırlarına (Rate Limit/429) takılmayı önleyen, akıllı anahtar rotasyonlu otonom Python arka plan motoru.
- **Akıllı Metin Parçalama (Chunking):** PDF'ler, anlamsal bütünlüğü korumak amacıyla `RecursiveCharacterTextSplitter` ile 1000 karakterlik parçalara ayrılır ve cümle ortası kesintileri önlemek için 200 karakterlik bindirmeler (overlap) yapılır.
- **Anlamsal Arama (Vector Retrieval):** Gelen sorular kelime kelime (keyword) aranmak yerine anlamsal olarak analiz edilir ve vektör deposundan (Supabase) en alakalı belgelerin paragrafları çekilir.
- **Rol Tabanlı LLM (System Prompt Mühendisliği):** Zeka modeline farklı departmanların görevleri (Örn: "Sen bir İK uzmanısın", "Sen tarafsız bir Arabulucusun") atanarak duruma özel uzman danışmanlık hizmeti sunulur.
- **Yapılandırılmış Çıktı (Structured Output):** Yapay zeka cevapları düz sohbet metni yerine, kurumun mobil uygulamasına veya intranete kolay entegre edilebilecek endüstri standartlarında (JSON) döner.

## 🛠️ Kullanılan Teknolojiler
- **Veri Yükleme ve İşleme (Python):** `PyPDFLoader`, `RecursiveCharacterTextSplitter`
- **Vektör Veritabanı:** Supabase (veya Pinecone uyumlu altyapı)
- **İş Akışı ve Orkestrasyon:** n8n (Chat Trigger, Vector Store Tools, Memory Nodes)
- **Yapay Zeka Modelleri:** Gelişmiş LLM'ler (DeepSeek, OpenAI vb.) ve Yerel/Bulut Embedding (vektör) modelleri.

## 📁 Proje Dosya Yapısı
- `upload_to_supabase.py`: PDF belgelerini okuyan, anlamsal parçalara bölen, vektöre (embedding) dönüştüren ve API limitlerine takılmadan veritabanına indeksleyen "Bilgi Rafinerisi" betiği.
- `RAG - PDF Ingestion (Veri Yükleme).json`: N8n üzerinden arayüzle veri yükleme işlemlerini kontrol eden iş akışı şablonu.
- `GooglePinecone(n8n).json`: Ön yüzdeki chat botunu yöneten, anlamsal arama yapan ve geçmiş hafızayı da (Chat Memory) katarak LLM ile son kararları veren Karar Motoru (Orchestration) iş akışı.
- `*.pdf`: Sistemin test edildiği, kurumsal bilginin çekildiği kapalı kaynak dokümanlar (Örn: Slicing_Pie_Handbook.pdf, O-C ANALİZİ.pdf).
- `yerel_embeddingler.jsonl`: Lokal ortamda üretilen test amaçlı vektör veri kayıtları.

## ⚙️ Nasıl Çalışır? (Sistem Akışı)
1. **Veri Yükleme (Arka Plan):** `upload_to_supabase.py` çalıştırılır. Şirketin PDF kılavuzları okunur, akıllıca parçalara ayrılır ve Supabase vektör veritabanına "bilgi uzayında koordinatlar" olarak indekslenir.
2. **Kullanıcı Tetiklemesi:** Kurum çalışanı n8n tabanlı bir arayüzden veya şirketin entegre chat botundan sorusunu yazar (Örn: "Arabuluculuk kuralları 3. maddeye göre ihlal nedir?").
3. **Anlamsal Arama:** N8n arkaplanı, soruyu anında vektöre dönüştürüp Supabase veritabanındaki şirket dokümanlarıyla çakıştırır ve sorunun cevabını içeren en doğru paragrafları (chunk'ları) bulup getirir.
4. **Cevap Üretimi:** Gelen paragraflar, şirketin kuralına göre ayarlanmış LLM'e (Yapay Zeka) aktarılır. Model sadece ama sadece bu belgeden yararlanarak kesin, net, halüsinasyonsuz ve kurumsal bir karar metni üretir.
