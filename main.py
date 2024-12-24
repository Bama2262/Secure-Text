from tkinter import *
from tkinter import messagebox
import base64

# Fungsi untuk enkripsi
def enkripsi():
    kata_sandi = kode.get()
    pesan = teks_input.get(1.0, END).strip()
    
    if not pesan:  # Validasi jika pesan kosong
        messagebox.showerror("Error", "Masukkan teks yang ingin dienkripsi")
        return
    
    if kata_sandi == "1234":
        pesan_terkode = pesan.encode("ascii")
        bytes_enkripsi = base64.b64encode(pesan_terkode)
        enkripsi = bytes_enkripsi.decode("ascii")
        tampilkan_hasil("ENKRIPSI", enkripsi, "#ed3833")
    elif kata_sandi == "":
        messagebox.showerror("Error", "Masukkan kata sandi")
    else:
        messagebox.showerror("Error", "Kata sandi tidak valid")

# Fungsi untuk dekripsi
def dekripsi():
    kata_sandi = kode.get()
    pesan = teks_input.get(1.0, END).strip()
    
    if not pesan:  # Validasi jika pesan kosong
        messagebox.showerror("Error", "Masukkan teks yang ingin didekripsi")
        return
    
    if kata_sandi == "1234":
        pesan_terkode = pesan.encode("ascii")
        try:
            bytes_dekripsi = base64.b64decode(pesan_terkode)
            dekripsi = bytes_dekripsi.decode("ascii")
            tampilkan_hasil("DEKRIPSI", dekripsi, "#00bd56")
        except Exception as e:
            messagebox.showerror("Error", f"Terjadi kesalahan saat dekripsi: {e}")
    elif kata_sandi == "":
        messagebox.showerror("Error", "Masukkan kata sandi")
    else:
        messagebox.showerror("Error", "Kata sandi tidak valid")

# Fungsi untuk menampilkan hasil enkripsi/dekripsi
def tampilkan_hasil(judul, hasil, warna):
    layar_hasil = Toplevel(layar)
    layar_hasil.title(judul)
    layar_hasil.geometry("400x200")
    layar_hasil.configure(bg=warna)

    Label(layar_hasil, text=judul, font="arial", fg="white", bg=warna).place(x=10, y=0)
    teks_output = Text(layar_hasil, font="Arial 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    teks_output.place(x=10, y=40, width=380, height=150)
    teks_output.insert(END, hasil)

# Fungsi untuk mereset program
def reset():
    kode.set("")
    teks_input.delete(1.0, END)

# Fungsi utama untuk antarmuka pengguna
def layar_utama():
    global layar
    global kode
    global teks_input
    layar = Tk()
    layar.geometry("375x398")
    layar.title("Program Enkripsi dan Dekripsi")

    # Label dan input teks
    Label(layar, text="Masukkan teks untuk enkripsi dan dekripsi", fg="black", font=("calibri", 13)).place(x=10, y=10)
    teks_input = Text(layar, font="Arial 13", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    teks_input.place(x=10, y=50, width=355, height=100)

    # Label dan input kata sandi
    Label(layar, text="Masukkan kata sandi (1234)", fg="black", font=("calibri", 13)).place(x=15, y=170)
    kode = StringVar()
    Entry(layar, textvariable=kode, width=19, bd=0, font=("arial", 25), show="*").place(x=15, y=200)

    # Tombol-tombol
    Button(layar, text="ENKRIPSI", height="2", width=23, bg="#ed3833", fg="black", bd=0, command=enkripsi).place(x=10, y=250)
    Button(layar, text="DEKRIPSI", height="2", width=23, bg="#00bd56", fg="black", bd=0, command=dekripsi).place(x=200, y=250)
    Button(layar, text="RESET PROGRAM", height="2", width=50, bg="#1089ff", fg="black", bd=0, command=reset).place(x=10, y=300)

    layar.mainloop()

# Menjalankan aplikasi
layar_utama()
