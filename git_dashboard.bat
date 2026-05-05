@echo off
:menu
cls
echo ======================================================
echo          GIT PROJE YONETIM PANELI
echo ======================================================
echo [1] Son 10 Versiyonu Gor (git log)
echo [2] Degisiklik Durumunu Kontrol Et (git status)
echo [3] Detayli Farklari Gor (git diff)
echo [4] Yeni Versiyon Kaydet (Commit Olustur)
echo [5] Uzak Sunucuya Gonder (git push)
echo [6] Cikis
echo ======================================================
set /p choice="Seciminizi yapin (1-6): "

if "%choice%"=="1" goto log
if "%choice%"=="2" goto status
if "%choice%"=="3" goto diff
if "%choice%"=="4" goto commit
if "%choice%"=="5" goto push
if "%choice%"=="6" goto exit
goto menu

:log
cls
echo --- SON 10 VERSIYON ---
git log --oneline -n 10
echo.
pause
goto menu

:status
cls
echo --- MEVCUT DURUM ---
git status
echo.
pause
goto menu

:diff
cls
echo --- DETAYLI DEGISIKLIKLER ---
git diff
echo.
pause
goto menu

:commit
cls
echo --- YENI VERSIYON KAYDI ---
powershell -ExecutionPolicy Bypass -File .\check_version.ps1
echo.
pause
goto menu

:push
cls
echo --- SUNUCUYA GONDERILIYOR ---
git push origin master
echo.
pause
goto menu

:exit
exit
