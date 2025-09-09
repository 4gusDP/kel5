# modul_web.py
# Kumpulan fungsi untuk program pemrograman web sederhana

# ================== LOGIN ==================
def input_login():
    user = input("Masukkan Username: ")
    pw = input("Masukkan Password: ")
    return user, pw

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
    return email, telepon

def cek_validasi(email, telepon):
    hasil = {}
    hasil["email"] = "valid" if "@" in email and "." in email else "tidak valid"
    hasil["telepon"] = "valid" if telepon.isdigit() and len(telepon) >= 10 else "tidak valid"
    return hasil

def output_validasi(hasil):
    print(f"Email: {hasil['email']}")
    print(f"Nomor Telepon: {hasil['telepon']}")

# ================== KASIR ==================
def input_kasir():
    n = int(input("Masukkan jumlah barang: "))
    barang = []
    for i in range(n):
        nama = input(f"Nama barang ke-{i+1}: ")
        harga = float(input(f"Harga {nama}: "))
        jumlah = int(input(f"Jumlah {nama}: "))
        barang.append((nama, harga, jumlah))
    return barang

def hitung_total(barang):
    total = 0
    rincian = []
    for nama, harga, jumlah in barang:
        subtotal = harga * jumlah
        total += subtotal
        rincian.append((nama, subtotal))
    return total, rincian

def output_kasir(total, rincian):
    for nama, subtotal in rincian:
        print(f"Subtotal {nama}: Rp{subtotal:.2f}")
    print(f"Total belanja: Rp{total:.2f}")

# ================== KONVERSI SATUAN ==================
def input_konversi():
    print("1. Panjang (meter → cm)")
    print("2. Berat (kg → gram)")
    print("3. Suhu (Celsius → Fahrenheit)")
    pilihan = input("Pilih konversi (1/2/3): ")
    nilai = float(input("Masukkan nilai yang akan dikonversi: "))
    return pilihan, nilai

def hitung_konversi(pilihan, nilai):
    if pilihan == "1":
        return nilai * 100, "cm"
    elif pilihan == "2":
        return nilai * 1000, "gram"
    elif pilihan == "3":
        return (nilai * 9/5) + 32, "°F"
    else:
        return None, None

def output_konversi(hasil, satuan):
    if hasil is not None:
        print(f"Hasil konversi: {hasil:.2f} {satuan}")
    else:
        print("Pilihan tidak valid!")
