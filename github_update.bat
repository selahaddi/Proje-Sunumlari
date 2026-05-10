@echo off
setlocal enabledelayedexpansion

echo ======================================================
echo           GITHUB GUNCELLEME ARACI
echo ======================================================

:: Degisiklikleri ekle
echo [+] Degisiklikler hazirlaniyor (git add .)
git add .

:: Commit mesaji iste
echo.
set /p commit_msg="Guncelleme notu girin (Bos birakilirsa 'Oto-Guncelleme' kullanilir): "

if "!commit_msg!"=="" (
    set commit_msg=Oto-Guncelleme
)

:: Kaydet
echo.
echo [+] Versiyon kaydediliyor...
git commit -m "!commit_msg!"

:: Gonder
echo.
echo [+] Uzak sunucudaki yeni degisiklikler aliniyor (git pull)...
git pull origin master

echo [+] GitHub'a gonderiliyor (git push)...
git push origin master

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ======================================================
    echo [BASARILI] Proje basariyla guncellendi!
    echo ======================================================
) else (
    echo.
    echo ======================================================
    echo [HATA] Bir sorun olustu. Lutfen internet baglantinizi ve git ayarlarini kontrol edin.
    echo ======================================================
)

echo.
pause
