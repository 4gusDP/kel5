# Program Permasalahan Pemrograman Web Sederhana
# Menggunakan Input, Percabangan, dan Perulangan

# Data login sederhana
USERNAME = "admin"
PASSWORD = "1234"

def login():
    print("\n=== Form Login ===")
    for i in range(3):  # maksimal 3 percobaan
        user = input("Masukkan Username: ")
        pw = input("Masukkan Password: ")
        if user == USERNAME and pw == PASSWORD:
            print("Login berhasil! ✅\n")
            return True
        else:
            print("Login gagal! Coba lagi.\n")
    print("Akses ditolak! 🚫")
    return False

def validasi_data():
    print("\n=== Validasi Data ===")
    email = input("Masukkan email: ")
    telepon = input("Masukkan nomor telepon: ")

    if "@" in email and "." in email:
        print("Email valid.")
    else:
        print("Email tidak valid!")

    if telepon.isdigit() and len(telepon) >= 10:
        print("Nomor telepon valid.")
    else:
        print("Nomor telepon tidak valid!")

def kasir():
    print("\n=== Aplikasi Kasir Sederhana ===")
    total = 0
    n = int(input("Masukkan jumlah barang: "))
    for i in range(n):
        nama = input(f"Nama barang ke-{i+1}: ")
        harga = float(input(f"Harga {nama}: "))
        jumlah = int(input(f"Jumlah {nama}: "))
        subtotal = harga * jumlah
        total += subtotal
        print(f"Subtotal {nama}: Rp{subtotal:.2f}")
    print(f"Total belanja: Rp{total:.2f}")

def konversi_satuan():
    print("\n=== Kalkulator Konversi Satuan ===")
    print("1. Panjang (meter → cm)")
    print("2. Berat (kg → gram)")
    print("3. Suhu (Celsius → Fahrenheit)")
    pilihan = input("Pilih konversi (1/2/3): ")

    if pilihan == "1":
        meter = float(input("Masukkan panjang (meter): "))
        print(f"Hasil: {meter*100} cm")
    elif pilihan == "2":
        kg = float(input("Masukkan berat (kg): "))
        print(f"Hasil: {kg*1000} gram")
    elif pilihan == "3":
        c = float(input("Masukkan suhu (Celsius): "))
        f = (c * 9/5) + 32
        print(f"Hasil: {f:.2f} °F")
    else:
        print("Pilihan tidak valid!")

# ================== PROGRAM UTAMA ==================
print("=== PROGRAM PEMROGRAMAN WEB SEDERHANA ===")

if login():
    ulang = "y"
    while ulang.lower() == "y":
        print("\nMenu:")
        print("1. Validasi Data (Email & Telepon)")
        print("2. Kasir Sederhana")
        print("3. Konversi Satuan")
        print("4. Keluar")
        menu = input("Pilih menu (1-4): ")

        if menu == "1":
            validasi_data()
        elif menu == "2":
            kasir()
        elif menu == "3":
            konversi_satuan()
        elif menu == "4":
            print("Terima kasih! Program selesai. 🙏")
            break
        else:
            print("Menu tidak tersedia!")

        ulang = input("\nApakah ingin kembali ke menu? (y/n): ")
