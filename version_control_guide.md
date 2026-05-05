# Git Versiyon Kontrol Rehberi

Bu rehber, projenizdeki değişiklikleri nasıl takip edeceğinizi ve yeni sürümler oluşturacağınızı açıklar.

## Temel İş Akışı

Bir değişiklik yaptıktan sonra şu adımları izleyin:

1. **Durumu Kontrol Edin:**
   ```bash
   git status
   ```
   Hangi dosyaların değiştiğini görmenizi sağlar.

2. **Değişiklikleri Sahneye Ekleyin:**
   ```bash
   git add .
   ```
   Tüm değişiklikleri bir sonraki sürüm (commit) için hazırlar.

3. **Yeni Sürüm (Commit) Oluşturun:**
   ```bash
   git commit -m "Yaptığınız değişikliğin kısa açıklaması"
   ```
   Değişiklikleri kalıcı bir sürüm olarak kaydeder.

4. **Geçmişi Görüntüleyin:**
   ```bash
   git log --oneline
   ```
   Şimdiye kadar oluşturulmuş tüm sürümleri listeler.

## İpuçları
- Her anlamlı değişiklikten sonra bir commit yapın.
- Commit mesajlarınız açıklayıcı olsun (Örn: "Ana sayfa renkleri güncellendi").
- Eğer bir hata yaparsanız, `git checkout .` ile son kaydedilen sürüme geri dönebilirsiniz (Dikkat: Kaydedilmemiş tüm değişiklikler silinir).

---
*Bu rehber Antigravity tarafından oluşturulmuştur.*
