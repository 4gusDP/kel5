# modul_web.py
# Kumpulan fungsi untuk program pemrograman web sederhana
# Menggunakan struktur data: list, dictionary, tuple

# ================== LOGIN ==================
def input_login():
    user = input("Masukkan Username: ")
    pw = input("Masukkan Password: ")
    return user, pw  # tuple (user, password)

def cek_login(user, pw):
    return user == "admin" and pw == "1234"

def output_login(status):
    if status:
        print("Login berhasil! ✅\n")
    else:
        print("Login gagal! 🚫\n")

# ================== VALIDASI DATA ==================
def input_validasi():
    email = input("Masukkan email: ")
    telepon = input("Masukkan nomor telepon: ")
    return email, telepon  # tuple (email, telepon)

def cek_validasi(email, telepon):
    hasil = {
        "email": "valid" if "@" in email and "." in email else "tidak valid",
        "telepon": "valid" if telepon.isdigit() and len(telepon) >= 10 else "tidak valid"
    }
    return hasil  # dictionary

def output_validasi(hasil):
    print(f"Email: {hasil['email']}")
    print(f"Nomor Telepon: {hasil['telepon']}")

# ================== KASIR ==================
def input_kasir():
    n = int(input("Masukkan jumlah barang: "))
    barang = []  # list
    for i in range(n):
        nama = input(f"Nama barang ke-{i+1}: ")
        harga = float(input(f"Harga {nama}: "))
        jumlah = int(input(f"Jumlah {nama}: "))
        barang.append((nama, harga, jumlah))  # tuple
    return barang  # list berisi tuple

def hitung_total(barang):
    total = 0
    rincian = []  # list
    for nama, harga, jumlah in barang:  # tuple unpacking
        subtotal = harga * jumlah
        total += subtotal
        rincian.append({"nama": nama, "subtotal": subtotal})  # dictionary
    return total, rincian

def output_kasir(total, rincian):
    for item in rincian:  # item adalah dictionary
        print(f"Subtotal {item['nama']}: Rp{item['subtotal']:.2f}")
    print(f"Total belanja: Rp{total:.2f}")

# ================== KONVERSI SATUAN ==================
def input_konversi():
    print("1. Panjang (meter → cm)")
    print("2. Berat (kg → gram)")
    print("3. Suhu (Celsius → Fahrenheit)")
    pilihan = input("Pilih konversi (1/2/3): ")
    nilai = float(input("Masukkan nilai yang akan dikonversi: "))
    return pilihan, nilai  # tuple

def hitung_konversi(pilihan, nilai):
    konversi = {  # dictionary untuk mapping
        "1": (nilai * 100, "cm"),
        "2": (nilai * 1000, "gram"),
        "3": ((nilai * 9/5) + 32, "°F")
    }
    return konversi.get(pilihan, (None, None))

def output_konversi(hasil, satuan):
    if hasil is not None:
        print(f"Hasil konversi: {hasil:.2f} {satuan}")
    else:
        print("Pilihan tidak valid!")
