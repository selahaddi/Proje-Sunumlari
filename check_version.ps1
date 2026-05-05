# Git Versiyon Kontrol Otomasyon Scripti

Write-Host "--- Proje Değişiklik Kontrolü ---" -ForegroundColor Cyan

# Mevcut durumu göster
$status = git status --short
if (-not $status) {
    Write-Host "Kaydedilecek bir değişiklik bulunamadı." -ForegroundColor Yellow
    exit
}

Write-Host "`nDeğişen dosyalar:" -ForegroundColor Green
git status --short

Write-Host "`nFarklar (Özet):" -ForegroundColor Green
git diff --stat

# Kullanıcıdan mesaj al
Write-Host "`nBu sürüm için bir açıklama girin (veya iptal için Enter'a basın):" -NoNewline
$message = Read-Host

if ([string]::IsNullOrWhiteSpace($message)) {
    Write-Host "İşlem iptal edildi." -ForegroundColor Red
    exit
}

# Git işlemlerini yap
Write-Host "`nDeğişiklikler kaydediliyor..." -ForegroundColor Cyan
git add .
git commit -m "$message"

Write-Host "`nYeni sürüm başarıyla oluşturuldu!" -ForegroundColor Green
git log --oneline -n 1
