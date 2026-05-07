graph LR
A[Code in JavaScript2<br/><small>(Yeni haberleri sıralayan node)</small>] -->|1. Yeni haberleri iletir| B(HTTP Request<br/><small>GitHub'dan Eski Dosyayı Çeker</small><br/><i>Execute Once AÇIK!</i>)

    B -->|2. Eski veriyi iletir| C(Haberleri Birleştir<br/><small>Yeni Code Node'u</small>)

    A -.->|3. Yeni haberleri arkadan çeker| C

    C -->|4. Tek bir fileContent metni iletir| D((GitHub Node<br/><small>Dosyayı Edit ile Günceller</small>))

    style A fill:#ffcc00,stroke:#333,stroke-width:2px,color:#000
    style B fill:#00d1b2,stroke:#333,stroke-width:2px,color:#fff
    style C fill:#ffcc00,stroke:#333,stroke-width:2px,color:#000
    style D fill:#333,stroke:#333,stroke-width:2px,color:#fff
