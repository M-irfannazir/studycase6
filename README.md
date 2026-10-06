<div align="center">

<h1 id="readme-top">SISTEM MANAJEMEN INVENTARIS BARANG</h1>

Aplikasi CLI berbasis Python untuk mencatat dan melihat stok barang di sebuah toko, dengan data yang disimpan permanen di file CSV.


**Nama : Muhammad Irfan Nazir | Kelas : B | NIM : 070**

</div>

---

## Daftar Isi

1. [Tentang Program](#tentang-program)
2. [Penjelasan Code](#penjelasan-code)
3. [Screenshot Output](#screenshot-output)

---

## Tentang Program

Program ini dibuat untuk membantu sebuah toko sederhana mendata barang yang masuk ke gudang. Data barang disimpan di file `inventaris.csv`, sehingga **tidak hilang** walaupun program dijalankan ulang.

Program berjalan terus menerus memakai `while True` sampai pengguna memilih keluar.

### Fitur

| Menu | Fitur | Keterangan |
|:---:|---|---|
| 1 | Lihat data barang | Membaca file CSV lalu menampilkan seluruh barang dalam bentuk tabel |
| 2 | Tambah barang baru | Menambahkan barang baru ke baris paling bawah file CSV |
| 3 | Keluar | Menghentikan program |

### Struktur File CSV

File `inventaris.csv` memiliki 4 kolom. Baris pertama adalah header.

```
NO,NAMA,STOK,HARGA
1,Indomie Goreng,120,3500
2,Gula Pasir 1kg,40,16000
3,Minyak Goreng 1L,25,18000
```

| Kolom | Keterangan |
|---|---|
| `NO` | Nomor barang, dibuat otomatis oleh program |
| `NAMA` | Nama barang (tidak boleh kosong) |
| `STOK` | Jumlah stok, harus berupa angka |
| `HARGA` | Harga barang dalam rupiah, harus berupa angka |


<p align="right">(<a href="#readme-top">back to top</a>)</p>


---

## Penjelasan Code

### 1. Library yang Digunakan

```python
import csv
from prettytable import PrettyTable
```

| Library | Kegunaan di program |
|---|---|
| `csv` | Membaca dan menulis file CSV |
| `prettytable` | Menampilkan data barang dalam bentuk tabel yang rapi |

### 2. Variabel Utama

```python
nama_file = "inventaris.csv"
```

Variabel `nama_file` menyimpan nama file CSV yang dipakai, jadi kalau nama file berubah cukup diganti di satu tempat.

### 3. Menu Utama

```python
while True:
    print("\n=== INVENTARIS BARANG TOKO ===")
    print("1. Lihat data barang")
    print("2. Tambah barang baru")
    print("3. Keluar")
    pilihan = input("Pilih menu (1-3): ")
```

- `while True` membuat menu tampil terus sampai pengguna memilih keluar.
- Pilihan dicek dengan `if / elif / else`.
- Pilihan 3 menjalankan `break` untuk menghentikan perulangan.

### 4. Menu 1: Lihat Data Barang

```python
data = []
with open(nama_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for row in csv_reader:
        data.append(row)
```

1. File dibuka dengan `open()`, lalu dibaca memakai `csv.reader`.
2. Setiap baris dimasukkan ke list `data` dengan `append()`.
3. `data[0]` adalah header. Kalau `len(data) <= 1`, berarti belum ada barang dan tampil pesan "Belum ada data barang."
4. Kalau ada data, program membuat `PrettyTable`. Header dijadikan nama kolom (`field_names`), lalu baris data ditambahkan satu per satu dengan `add_row()`.

```python
tabel = PrettyTable()
tabel.field_names = data[0]
for baris in data[1:]:
    tabel.add_row(baris)
print(tabel)
```

### 5. Menu 2: Tambah Barang Baru

**a. Menentukan nomor barang**

File dibaca dulu seperti di menu 1. Jumlah baris di file (termasuk header) dipakai sebagai nomor barang baru:

```python
no = len(data)
```

Contohnya, kalau di file ada header dan 3 barang, `len(data)` bernilai 4 sehingga barang baru mendapat nomor 4.

**b. Input dan validasi**

| Input | Aturan | Cara cek |
|---|---|---|
| Nama barang | Tidak boleh kosong | `nama.strip() == ""` |
| Stok | Harus angka | `stok.isdigit()` |
| Harga | Harus angka | `harga.isdigit()` |

Setiap input memakai `while`, jadi pengguna diminta mengisi ulang terus sampai inputnya benar.

```python
stok = input("Stok : ")
while not stok.isdigit():
    print("Stok harus berupa angka!")
    stok = input("Stok : ")
```

**c. Menyimpan ke file CSV**

```python
with open(nama_file, mode="a", newline="") as csv_file:
    writer = csv.writer(csv_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow([no, nama, stok, harga])
```

| Bagian | Fungsi |
|---|---|
| `mode="a"` | Mode append, data baru ditambahkan di bawah tanpa menghapus data lama, sehingga data tersimpan permanen |
| `newline=""` | Mencegah muncul baris kosong di antara data |
| `csv.writer` | Menulis data ke file CSV |
| `writerow([...])` | Menulis satu baris data (no, nama, stok, harga) |

### 6. Menu 3: Keluar

```python
elif pilihan == "3":
    print("Program selesai. Terima kasih!")
    break
```

`break` menghentikan `while True` sehingga program selesai.

### 7. Pilihan Tidak Valid

```python
else:
    print("Pilihan tidak ada, coba lagi.")
```

Kalau pengguna mengetik selain 1, 2, atau 3, program menampilkan pesan dan kembali ke menu.

### 8. Konsep Pemrograman yang Digunakan

| Konsep | Contoh di program |
|---|---|
| Variabel dan tipe data | `nama_file`, `pilihan`, `nama`, `stok`, `harga` |
| Operator | `==`, `<=`, `not` |
| Conditional statement | `if / elif / else` pada menu dan validasi |
| Looping | `while True` pada menu dan validasi input, `for` pada pembacaan file dan tabel |
| List | `data` untuk menampung seluruh baris dari file CSV |
| File handling (CSV) | `csv.reader` untuk membaca, `csv.writer` dengan mode `a` untuk menulis |
| Library | `csv`, `prettytable` |


<p align="right">(<a href="#readme-top">back to top</a>)</p>


---

## Screenshot Output

Berikut tampilan program saat dijalankan di terminal.

### 1. Menu Utama

<img width="291" height="133" alt="Screenshot 2026-10-06 200335" src="https://github.com/user-attachments/assets/7ccecfac-9180-4226-b25c-14608e630e6b" />

Program menampilkan tiga pilihan menu: Lihat data barang, Tambah barang baru, dan Keluar.

### 2. Lihat Data Barang

- data barang sebelum ditambahkan

<img width="282" height="283" alt="Screenshot 2026-10-06 200359" src="https://github.com/user-attachments/assets/9ec9f952-1c97-4f3f-9dcf-97ff417e1517" />

- data baramg setelah ditambah

<img width="234" height="205" alt="Screenshot 2026-10-06 201046" src="https://github.com/user-attachments/assets/b046eed5-21cf-42ab-a940-7a79eec295e6" />

Seluruh data barang dari file CSV ditampilkan dalam bentuk tabel.

### 3. Tambah Barang Baru

<img width="202" height="140" alt="Screenshot 2026-10-06 200957" src="https://github.com/user-attachments/assets/5e3e21a3-2268-4093-9236-dbe167b3bdad" />

Pengguna mengisi nama, stok, dan harga, lalu muncul pesan "Barang berhasil ditambahkan!".

### 4. Validasi Input

<img width="187" height="206" alt="Screenshot 2026-10-06 201032" src="https://github.com/user-attachments/assets/a16cb9fd-6977-4d53-8eff-312e6bbaea70" />

Kalau stok atau harga bukan angka, atau nama dikosongkan, program menolak input dan meminta mengisi ulang.

### 5. Data Tersimpan di File CSV

- awal `file csv`

<img width="523" height="185" alt="Screenshot 2026-10-06 200240" src="https://github.com/user-attachments/assets/564bbb17-7187-4e6b-ad03-8949f211814a" />

- setelah data baru ditambahkan ke `file csv`

<img width="523" height="185" alt="Screenshot 2026-10-06 201322" src="https://github.com/user-attachments/assets/e47f33f9-e556-4156-a6f3-7f2da5084729" />

Barang yang baru ditambahkan muncul di file `inventaris.csv` dan tetap ada saat program dijalankan ulang.

### 6. Keluar dari Program

<img width="340" height="107" alt="Screenshot 2026-10-06 201058" src="https://github.com/user-attachments/assets/e5d2b7e7-5182-431a-a8cd-96f112c3e43a" />

Setelah memilih menu 3, program menampilkan pesan terima kasih lalu berhenti.


<p align="right">(<a href="#readme-top">back to top</a>)</p>


---
