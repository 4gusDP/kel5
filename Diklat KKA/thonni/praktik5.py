import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np

# ============================
# Fungsi Hitung Hambatan
# ============================
def hitung_hambatan():
    # Ambil nilai R1 dan R2 dari slider
    R1 = slider_R1.get()
    R2 = slider_R2.get()
    
    # Ambil pilihan rangkaian (seri / paralel)
    pilihan = rangkaian.get()
    
    # Hitung nilai total sesuai pilihan
    if pilihan == "Seri":
        R_total = R1 + R2
    else:  # Paralel
        if R1 == 0 or R2 == 0:
            R_total = 0
        else:
            R_total = 1 / ((1 / R1) + (1 / R2))
    
    # Tampilkan hasil pada label
    hasil_label.config(text=f"Nilai Total Hambatan: {R_total:.2f} Ω")
    
    # Gambar grafik hubungan
    gambar_grafik(R1, R2, pilihan)

# ============================
# Fungsi Gambar Grafik
# ============================
def gambar_grafik(R1, R2, pilihan):
    # Buat rentang nilai R2 dari 1 sampai 100000
    R2_range = np.linspace(1, 100000, 200)
    
    # Hitung hambatan total untuk semua nilai R2
    if pilihan == "Seri":
        R_total = R1 + R2_range
    else:  # Paralel
        R_total = 1 / ((1 / R1) + (1 / R2_range))
    
    # Buat grafik
    plt.figure(figsize=(7, 5))
    plt.plot(R2_range, R_total, label=f"R1 = {R1} Ω, Mode = {pilihan}")
    plt.scatter([R2], [R1+R2 if pilihan=="Seri" else 1/((1/R1)+(1/R2))], 
                color='red', label=f"R2 = {R2} Ω (dipilih)")
    
    # Atur sumbu
    plt.xlabel("R2 (Ohm)")
    plt.ylabel("R_total (Ohm)")
    plt.title("Grafik Hubungan R2 vs Hambatan Total")
    plt.grid(True)
    plt.legend()
    plt.show()

# ============================
# GUI Tkinter
# ============================
root = tk.Tk()
root.title("Kalkulator Hambatan Dua Resistor")
root.geometry("500x400")

# Label Judul
ttk.Label(root, text="Kalkulator Hambatan R1 dan R2", font=("Arial", 14, "bold")).pack(pady=10)

# Slider R1
ttk.Label(root, text="Resistor R1 (Ohm)").pack()
slider_R1 = tk.Scale(root, from_=0, to=100000, orient="horizontal", length=400)
slider_R1.pack(pady=5)

# Slider R2
ttk.Label(root, text="Resistor R2 (Ohm)").pack()
slider_R2 = tk.Scale(root, from_=0, to=100000, orient="horizontal", length=400)
slider_R2.pack(pady=5)

# Option button untuk pilihan rangkaian
rangkaian = tk.StringVar(value="Seri")
ttk.Label(root, text="Pilih Jenis Rangkaian:").pack(pady=5)
ttk.Radiobutton(root, text="Seri", variable=rangkaian, value="Seri").pack()
ttk.Radiobutton(root, text="Paralel", variable=rangkaian, value="Paralel").pack()

# Tombol Hitung
hitung_btn = ttk.Button(root, text="Hitung Hambatan", command=hitung_hambatan)
hitung_btn.pack(pady=10)

# Label hasil
hasil_label = ttk.Label(root, text="Nilai Total Hambatan: -", font=("Arial", 12))
hasil_label.pack(pady=10)

# Jalankan aplikasi
root.mainloop()
