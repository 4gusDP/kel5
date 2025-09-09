import tkinter as tk
from tkinter import ttk

# Dictionary kode warna resistor
digit_colors = {
    "Hitam": 0, "Coklat": 1, "Merah": 2, "Oranye": 3,
    "Kuning": 4, "Hijau": 5, "Biru": 6, "Ungu": 7,
    "Abu-abu": 8, "Putih": 9
}

multiplier_colors = {
    "Hitam": 1, "Coklat": 10, "Merah": 100, "Oranye": 1_000,
    "Kuning": 10_000, "Hijau": 100_000, "Biru": 1_000_000,
    "Ungu": 10_000_000, "Emas": 0.1, "Perak": 0.01
}

tolerance_colors = {
    "Coklat": "±1%", "Merah": "±2%", "Emas": "±5%",
    "Perak": "±10%", "Tanpa gelang": "±20%"
}

# Fungsi untuk menghitung nilai resistor
def hitung_resistor():
    # Ambil pilihan dari dropdown
    g1 = combo1.get()
    g2 = combo2.get()
    g3 = combo3.get()
    g4 = combo4.get()
    
    # Hitung nilai berdasarkan kode warna
    digit1 = digit_colors[g1]
    digit2 = digit_colors[g2]
    multiplier = multiplier_colors[g3]
    tolerance = tolerance_colors[g4]
    
    nilai = (digit1 * 10 + digit2) * multiplier
    
    # Tampilkan hasil
    hasil_label.config(
        text=f"Nilai Resistor: {nilai} Ω {tolerance}"
    )

# Membuat jendela utama
root = tk.Tk()
root.title("Kalkulator Resistor 4 Gelang Warna")
root.geometry("400x300")

# Label dan dropdown untuk gelang warna
ttk.Label(root, text="Gelang 1 (Digit Pertama):").pack(pady=5)
combo1 = ttk.Combobox(root, values=list(digit_colors.keys()))
combo1.pack()

ttk.Label(root, text="Gelang 2 (Digit Kedua):").pack(pady=5)
combo2 = ttk.Combobox(root, values=list(digit_colors.keys()))
combo2.pack()

ttk.Label(root, text="Gelang 3 (Pengali):").pack(pady=5)
combo3 = ttk.Combobox(root, values=list(multiplier_colors.keys()))
combo3.pack()

ttk.Label(root, text="Gelang 4 (Toleransi):").pack(pady=5)
combo4 = ttk.Combobox(root, values=list(tolerance_colors.keys()))
combo4.pack()

# Tombol untuk menghitung
hitung_btn = ttk.Button(root, text="Hitung", command=hitung_resistor)
hitung_btn.pack(pady=10)

# Label hasil
hasil_label = ttk.Label(root, text="Nilai Resistor: -")
hasil_label.pack(pady=10)

# Jalankan aplikasi
root.mainloop()
