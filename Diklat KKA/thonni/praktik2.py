# Program Menghitung Hambatan Total dari Dua Resistor (R1 dan R2)
# dengan pilihan Rangkaian Seri atau Paralel

# Meminta input nilai resistor dari pengguna
R1 = float(input("Masukkan nilai resistor R1 (Ohm): "))   # input nilai R1
R2 = float(input("Masukkan nilai resistor R2 (Ohm): "))   # input nilai R2

# Menampilkan pilihan jenis rangkaian
print("\nPilih jenis rangkaian:")
print("1. Seri")
print("2. Paralel")

pilihan = input("Masukkan pilihan (1/2): ")   # pengguna memilih jenis rangkaian

# Menghitung hambatan total sesuai pilihan
if pilihan == "1":
    # Rangkaian Seri: R_total = R1 + R2
    R_total = R1 + R2
    print(f"\nRangkaian Seri: R_total = {R1} + {R2} = {R_total} Ohm")

elif pilihan == "2":
    # Rangkaian Paralel: 1/R_total = 1/R1 + 1/R2
    R_total = 1 / ((1/R1) + (1/R2))
    print(f"\nRangkaian Paralel: R_total = 1 / (1/{R1} + 1/{R2}) = {R_total} Ohm")

else:
    # Jika pilihan tidak valid
    print("\nPilihan tidak valid. Silakan jalankan program lagi.")
