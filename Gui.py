import tkinter as tk
from tkinter import messagebox

# Fungsi untuk menampilkan hasil prediksi
def hasil_prediksi():
    hasil_label.config(text="Prodi: Teknologi Informasi")

# Membuat jendela utama
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("400x500")

# Label Judul
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16, "bold"))
judul_label.pack(pady=10)

# Membuat Frame untuk menampung input nilai mata pelajaran
frame_nilai = tk.Frame(root)
frame_nilai.pack(pady=10)

# Membuat 10 label dan input nilai mata pelajaran
input_nilai = []
for i in range(1, 11):
    # Label untuk nama mata pelajaran
    label = tk.Label(frame_nilai, text=f"Nilai Mata Pelajaran {i}:")
    label.grid(row=i-1, column=0, padx=5, pady=5, sticky="e")
    
    # Entry untuk nilai mata pelajaran
    entry = tk.Entry(frame_nilai)
    entry.grid(row=i-1, column=1, padx=5, pady=5)
    input_nilai.append(entry)

# Button untuk menampilkan hasil prediksi
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi)
prediksi_button.pack(pady=20)

# Label untuk menampilkan hasil prediksi
hasil_label = tk.Label(root, text="", font=("Arial", 14))
hasil_label.pack(pady=10)

# Menjalankan GUI
root.mainloop()
