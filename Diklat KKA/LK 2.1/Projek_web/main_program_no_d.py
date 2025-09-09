# main_program.py
# Program utama menggunakan modul_web.py

import modul_web_no_d as mw

print("=== PROGRAM PEMROGRAMAN WEB SEDERHANA ===")

# Proses login dengan maksimal 3 kali percobaan
login_berhasil = False
for i in range(3):
    user, pw = mw.input_login()   # tuple
    login_berhasil = mw.cek_login(user, pw)
    mw.output_login(login_berhasil)
    if login_berhasil:
        break

if login_berhasil:
    ulang = "y"
    while ulang.lower() == "y":
        print("\nMenu:")
        print("1. Validasi Data (Email & Telepon)")
        print("2. Kasir Sederhana")
        print("3. Konversi Satuan")
        print("4. Keluar")
        menu = input("Pilih menu (1-4): ")

        if menu == "1":
            email, telepon = mw.input_validasi()  # tuple
            hasil = mw.cek_validasi(email, telepon)  # dictionary
            mw.output_validasi(hasil)

        elif menu == "2":
            barang = mw.input_kasir()  # list berisi tuple
            total, rincian = mw.hitung_total(barang)  # rincian berupa list of dictionary
            mw.output_kasir(total, rincian)

        elif menu == "3":
            pilihan, nilai = mw.input_konversi()  # tuple
            hasil, satuan = mw.hitung_konversi(pilihan, nilai)  # tuple
            mw.output_konversi(hasil, satuan)

        elif menu == "4":
            print("Terima kasih! Program selesai. 🙏")
            break
        else:
            print("Menu tidak tersedia!")

        ulang = input("\nApakah ingin kembali ke menu? (y/n): ")
else:
    print("Program ditutup karena login gagal 3 kali.")
