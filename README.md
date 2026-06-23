<div align="center">

# 🔑 Serial Number Generator (SNG Pro)

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)
![Android](https://img.shields.io/badge/Platform-Android-3DDC84?style=for-the-badge&logo=android&logoColor=white)
![Repo Size](https://img.shields.io/github/repo-size/useripx/04-SN?style=for-the-badge&color=blue)
![Version](https://img.shields.io/badge/Version-1.5-blue?style=for-the-badge)
![License](https://img.shields.io/badge/License-Free-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Selesai-brightgreen?style=for-the-badge)
![PyInstaller](https://img.shields.io/badge/Build-PyInstaller-orange?style=for-the-badge&logo=pyinstaller&logoColor=white)
![Kivy](https://img.shields.io/badge/GUI-Kivy-darkblue?style=for-the-badge)
![Inno Setup](https://img.shields.io/badge/Installer-Inno_Setup-7289DA?style=for-the-badge)
![Semester](https://img.shields.io/badge/Semester-1-blueviolet?style=for-the-badge)

**Generator Serial Number dengan 2 mode: Random & Encrypt (Caesar Cipher). Tersedia versi CLI, GUI Desktop, dan Android.**

*Dibuat oleh Yogi Ario — Proyek Semester 1*

---

</div>

## 📖 Deskripsi

Aplikasi **Serial Number Generator** (SNG Pro) v1.5 yang dapat menghasilkan serial number dengan dua metode:

1. **Random Serial** — menghasilkan serial number acak dari kombinasi huruf dan angka.
2. **Encrypt Kata** — mengubah input teks menjadi kode unik menggunakan **Caesar Cipher** dengan pergeseran +6.

Program tersedia dalam **3 versi**: CLI (terminal), GUI Desktop (Kivy), dan Android (APK via Buildozer).

## ✨ Fitur

- 🎲 **Generate Serial Random** — serial acak dengan panjang custom
- 🔐 **Encrypt Kata** — Caesar Cipher shift +6 untuk huruf dan angka
- 🖥️ **Versi CLI** — `sngpt.py` (dengan admin privilege) & `sngemini.py`
- 📱 **Versi Android (Kivy)** — GUI mobile dengan Buildozer
- 🛡️ **Auto Admin Privilege** — request Run as Administrator otomatis (versi GPT)
- ♻️ Loop untuk membuat serial berulang kali
- 📦 Tersedia installer (Inno Setup, MSI x86/x64, ZIP)

## 📁 Struktur Proyek

```
04 SN/
├── sngpt.py               # Source CLI + admin privilege (versi GPT)
├── sngemini.py             # Source CLI tanpa admin (versi Gemini)
├── main.py                 # Entry point (import dari sngpt)
├── sngpt.spec              # Konfigurasi PyInstaller
├── SN.iss                  # Script Inno Setup installer
├── setup.exe               # Installer Inno Setup
├── img.ico                 # Icon aplikasi
├── Icon.ico                # Icon alternatif
├── apk/                    # Versi Android (Kivy)
│   ├── SN.py               # Source code GUI (Kivy App)
│   └── buildozer.spec      # Konfigurasi Buildozer
├── build/                  # File build PyInstaller
├── dist/
│   ├── SNG.exe             # Executable standalone
│   ├── setup.exe           # Installer Inno Setup
│   ├── setup x64.msi       # Installer MSI 64-bit
│   ├── setup x86.msi       # Installer MSI 32-bit
│   └── dist.zip            # Distribusi ZIP
└── __pycache__/            # Cache Python
```

## 🚀 Cara Menjalankan

### Opsi 1: Jalankan file Python (CLI)

```bash
# Versi dengan admin privilege
python sngpt.py

# Versi tanpa admin
python sngemini.py
```

### Opsi 2: Jalankan Executable

Buka `dist/SNG.exe` langsung (tanpa perlu install Python).

### Opsi 3: Install via Installer

| Installer | Lokasi |
|-----------|--------|
| Inno Setup | `setup.exe` (root) |
| MSI 64-bit | `dist/setup x64.msi` |
| MSI 32-bit | `dist/setup x86.msi` |

### Opsi 4: Build untuk Android

```bash
cd apk
pip install buildozer kivy
buildozer android debug
```

### Opsi 5: Build ulang executable

```bash
pip install pyinstaller
pyinstaller sngpt.spec
```

## 📸 Contoh Penggunaan

### Mode 1 — Generate Serial Random

```
Serial number maker v1.0
Terimakasih untuk:
Yogi Ario

Pilih salah satu:
1. Generate Serial
2. Encrypt Kata
Masukkan pilihan Anda (1/2): 1
Masukkan panjang serial number yang diinginkan: 16
Serial number acak: kZ9xLm2QpR4wN8yT
```

### Mode 2 — Encrypt Kata (Caesar Cipher +6)

```
Pilih salah satu:
1. Generate Serial
2. Encrypt Kata
Masukkan pilihan Anda (1/2): 2
Masukkan kata, kalimat, dan atau angka Anda: YogiArio2024
Serial number Random: EumoGxou8680
```

## 📝 Perbedaan Versi File

| File | Tipe | Admin | Deskripsi |
|------|------|-------|-----------|
| `sngpt.py` | CLI | ✅ Ya | Versi lengkap dengan auto-admin privilege |
| `sngemini.py` | CLI | ❌ Tidak | Versi ringan dengan docstring |
| `apk/SN.py` | GUI (Kivy) | ❌ Tidak | Versi Android dengan UI grafis |
| `main.py` | Entry | — | Import & jalankan dari `sngpt.py` |

## 🛠️ Teknologi

| Komponen | Detail |
|----------|--------|
| Bahasa | Python 3.x |
| Library | `random`, `string`, `ctypes` (built-in) |
| GUI Framework | Kivy (versi Android) |
| Algoritma | Random generation, Caesar Cipher (shift +6) |
| Build Tool | PyInstaller (Windows), Buildozer (Android) |
| Installer | Inno Setup, MSI |
| Platform | Windows, Android |

## 👤 Author

**Yogi Ario**
🌐 [Website](https://userutgc.github.io/yogiariohomeconnection/)

---

<div align="center">

*Proyek Mata Kuliah — Semester 1 — Teknik Informatika UNP*

</div>
