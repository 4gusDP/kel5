import tkinter as tk
from tkinter import ttk

# ==============================
# Dictionary Warna Resistor
# ==============================

# Digit pertama & kedua
digit_colors = {
    "Hitam": 0, "Coklat": 1, "Merah": 2, "Oranye": 3,
    "Kuning": 4, "Hijau": 5, "Biru": 6, "Ungu": 7,
    "Abu-abu": 8, "Putih": 9
}

# Faktor pengali
multiplier_colors = {
    "Hitam": 1, "Coklat": 10, "Merah": 100, "Oranye": 1_000,
    "Kuning": 10_000, "Hijau": 100_000, "Biru": 1_000_000,
    "Ungu": 10_000_000, "Emas": 0.1, "Perak": 0.01
}

# Toleransi
tolerance_colors = {
    "Coklat": "±1%", "Merah": "±2%", "Hijau": "±0.5%",
    "Biru": "±0.25%", "Ungu": "±0.1%", "Abu-abu": "±0.05%",
    "Emas": "±5%", "Perak": "±10%", "Tanpa gelang": "±20%"
}

# Warna tampilan (RGB/HEX) untuk kotak warna
color_display = {
    "Hitam": "#000000", "Coklat": "#8B4513", "Merah": "#FF0000",
    "Oranye": "#FFA500", "Kuning": "#FFFF00", "Hijau": "#008000",
    "Biru": "#0000FF", "Ungu": "#800080", "Abu-abu": "#808080",
    "Putih": "#FFFFFF", "Emas": "#FFD700", "Perak": "#C0C0C0",
    "Tanpa gelang": "#F5F5F5"
}

# ==============================
# Fungsi Hitung Resistor
# ==============================
def hitung_resistor():
    # Ambil warna dari dropdown
    g1 = combo1.get()
    g2 = combo2.get()
    g3 = combo3.get()
    g4 = combo4.get()
    
    # Validasi input
    if g1 == "" or g2 == "" or g3 == "" or g4 == "":
        hasil_label.config(text="Silakan pilih semua gelang terlebih dahulu.")
        return
    
    # Hitung nilai resistor
    digit1 = digit_colors[g1]
    digit2 = digit_colors[g2]
    multiplier = multiplier_colors[g3]
    tolerance = tolerance_colors[g4]
    
    nilai = (digit1 * 10 + digit2) * multiplier
    
    # Tampilkan hasil
    hasil_label.config(
        text=f"Nilai Resistor: {nilai} Ω {tolerance}"
    )

# ==============================
# Fungsi Update Warna Preview
# ==============================
def update_warna():
    warna1.config(bg=color_display.get(combo1.get(), "white"))
    warna2.config(bg=color_display.get(combo2.get(), "white"))
    warna3.config(bg=color_display.get(combo3.get(), "white"))
    warna4.config(bg=color_display.get(combo4.get(), "white"))

# ==============================
# GUI Tkinter
# ==============================
root = tk.Tk()
root.title("Kalkulator Resistor 4 Gelang Warna")
root.geometry("500x400")

# Label instruksi
ttk.Label(root, text="Pilih Warna Gelang Resistor", font=("Arial", 12, "bold")).pack(pady=10)

# Frame untuk dropdown dan preview warna
frame = tk.Frame(root)
frame.pack(pady=10)

# Dropdown Gelang 1
ttk.Label(frame, text="Gelang 1 (Digit 1):").grid(row=0, column=0, sticky="w", padx=5, pady=5)
combo1 = ttk.Combobox(frame, values=list(digit_colors.keys()), width=15)
combo1.grid(row=0, column=1, padx=5)
warna1 = tk.Label(frame, width=10, height=1, relief="solid")
warna1.grid(row=0, column=2, padx=5)

# Dropdown Gelang 2
ttk.Label(frame, text="Gelang 2 (Digit 2):").grid(row=1, column=0, sticky="w", padx=5, pady=5)
combo2 = ttk.Combobox(frame, values=list(digit_colors.keys()), width=15)
combo2.grid(row=1, column=1, padx=5)
warna2 = tk.Label(frame, width=10, height=1, relief="solid")
warna2.grid(row=1, column=2, padx=5)

# Dropdown Gelang 3
ttk.Label(frame, text="Gelang 3 (Pengali):").grid(row=2, column=0, sticky="w", padx=5, pady=5)
combo3 = ttk.Combobox(frame, values=list(multiplier_colors.keys()), width=15)
combo3.grid(row=2, column=1, padx=5)
warna3 = tk.Label(frame, width=10, height=1, relief="solid")
warna3.grid(row=2, column=2, padx=5)

# Dropdown Gelang 4
ttk.Label(frame, text="Gelang 4 (Toleransi):").grid(row=3, column=0, sticky="w", padx=5, pady=5)
combo4 = ttk.Combobox(frame, values=list(tolerance_colors.keys()), width=15)
combo4.grid(row=3, column=1, padx=5)
warna4 = tk.Label(frame, width=10, height=1, relief="solid")
warna4.grid(row=3, column=2, padx=5)

# Tombol Hitung
hitung_btn = ttk.Button(root, text="Hitung Nilai Resistor", command=hitung_resistor)
hitung_btn.pack(pady=10)

# Tombol Update Warna
update_btn = ttk.Button(root, text="Tampilkan Warna Gelang", command=update_warna)
update_btn.pack(pady=5)

# Label Hasil
hasil_label = ttk.Label(root, text="Nilai Resistor: -", font=("Arial", 12))
hasil_label.pack(pady=20)

# Jalankan aplikasi
root.mainloop()
