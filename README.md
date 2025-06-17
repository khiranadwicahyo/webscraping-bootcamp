# webscraping-bootcamp
# 🕸️ Webscraping Bootcamp

Selamat datang di proyek `webscraping-bootcamp`, sebuah repositori latihan pribadi saya untuk mempelajari scraping data dari web menggunakan tiga alat utama:
- `BeautifulSoup` (untuk situs statis)
- `Selenium` (untuk situs dinamis & JavaScript)
- `Scrapy` (untuk crawling otomatis berskala besar, coming soon)

---

## 📚 Struktur Pembelajaran

### 1. `basic_tutorial_scrape.ipynb`
Dalam file jupyter ini saya akan memberikan contoh syntax dasar yang perlu diketahui untuk memulai melakukan scraping pada bs4 dan selenium.

### 2. `bs4_basics.ipynb`
Dalam file jupyter ini saya akan memberikan Contoh penggunaan BeautifulSoup untuk melakukan scraping HTML statis seperti artikel, tabel, dan pagination sekaligus menyimpannya ke dalam file CSV.

### 3. `selenium_basics.ipynb`
Dalam file Jupyter ini saya akan memberikan Contoh penggunaan selenium untuk scraping dari website dinamis, klik tombol, login otomatis, dan simpan ke CSV.

### 4. `scrapy_project/`
Dalam folder ini kita akan mencoba untuk setup scrapy sekaligus spiders untuk bisa melakukan crawling data. Crawling data yang akan dilakukan mulai dari mencoba melakukan crawling elemen sederhana hingga crwaling setiap halaman dan export ke format yang dibutuhkan.

---

## 🧪 Requirement & Setup
### Requirements
Versi : (Python 3.10.7)
```txt
scrapy==2.11.1
pandas==2.2.2
openpyxl==3.1.2
beautifulsoup4==4.12.3
selenium==4.20.0
fake-useragent==1.5.1
python-dotenv==1.0.1
```

### Buat environment
Untuk kebutuhan yang lebih fleksibel pada versi python yang anda miliki, dengan cara menuliskan kode berikut:

```bash
python -m venv env # Windows 
python3 -m venv env # MacOS
```
`env` adalah nama virtual environment, anda bisa gunakan nama lain sesuai kebutuhan.

Jika Python anda sama dengan saya, anda bisa langsung melakukan install menggunakan file `requirements.txt` yang sudah saya buat.

Jangan lupa untuk mengaktifkan virtual environment terlebih dahulu dengan cara:
```bash
env\Srcipts\activate # Windows
source env\bin\activate # MacOS
```
lalu ketik perintah dibawah ini untuk memulai install `requirements.txt`:
```bash
pip install -r requirements.txt
```
anda juga bisa memastikan package yang telah terinstall dengan cara:
```bash
pip list
```
jika setup telah selali anda bisa menon-aktifkan virtual environment dengan cara:
```bash
deactivate
```

**Tambahan:** Ketika anda menggunakan virtual enviroment, cek apakah sudah terdapat di jupyter kernel anda. Jika belum terdaftar di kernel, anda bisa menginstall ipykernel dan daftarkan env ke kernel dengan membuat name dan display name agar terlihat di vscode. Berikut perintah yang digunakan:

```bash
pip install ipykernel
python -m ipykernel install --user --name=myenv --display-name "Python (scrapy-env)"
```
