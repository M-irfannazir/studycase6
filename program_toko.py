import csv
from prettytable import PrettyTable

nama_file = "inventaris.csv"

while True:
    print("\n=== INVENTARIS BARANG TOKO ===")
    print("1. Lihat data barang")
    print("2. Tambah barang baru")
    print("3. Keluar")
    pilihan = input("Pilih menu (1-3): ")

    if pilihan == "1":
        data = []
        with open(nama_file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            for row in csv_reader:
                data.append(row)

        if len(data) <= 1:
            print("Belum ada data barang.")
        else:
            tabel = PrettyTable()
            tabel.field_names = data[0]
            for baris in data[1:]:
                tabel.add_row(baris)
            print(tabel)

    elif pilihan == "2":
        data = []
        with open(nama_file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            for row in csv_reader:
                data.append(row)
        no = len(data)

        nama = input("Nama barang : ")
        while nama.strip() == "":
            print("Nama barang tidak boleh kosong!")
            nama = input("Nama barang : ")

        stok = input("Stok : ")
        while not stok.isdigit():
            print("Stok harus berupa angka!")
            stok = input("Stok : ")

        harga = input("Harga (Rp) : ")
        while not harga.isdigit():
            print("Harga harus berupa angka!")
            harga = input("Harga (Rp) : ")

        with open(nama_file, mode="a", newline="") as csv_file:
            writer = csv.writer(csv_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([no, nama, stok, harga])

        print("Barang berhasil ditambahkan!")

    elif pilihan == "3":
        print("Program selesai. Terima kasih!")
        break

    else:
        print("Pilihan tidak ada, coba lagi.")