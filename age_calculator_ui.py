from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror
from datetime import date


# fungsi untuk menghitung umur
def calculate_age():
    #  Try/except
    try:
        # mendapatkan tanggal saat ini
        today = date.today()
        # mendapatkan hari dari entry hari 
        day = int(day_entry.get())
        # mendapatkan bulan dari entry bulan
        month = int(month_entry.get())
        # mendapatkan tahun dari entry tahun
        year = int(year_entry.get())
        # membuat objek tanggal
        birthdate = date(year, month, day)
        # menghitung umur
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        # menampilkan usia menggunakan label hasil usia
        age_result.config(text='Sekarang umur kamu ' + str(age) + ' tahun')
    # jika terjadi kesalahan jendela showerror akan muncul
    except:
        showerror(title='Error', message='Terjadi kesalahan saat mencoba menghitung umur ' \
                    '\nBerikut ini bisa ' \
                    'Di karenakan:\n->Gagal memasukan data\n->Ada bidang yang kosong \n'\
                     'Pastikan Anda memasukkan data yang valid')



# membuat jendela utama
window = Tk()
# judul untuk jendela
window.title('Kelompok Koker')
# dimensi dan posisi jendela
window.geometry('500x260+430+300')
# membuat jendela nonresizabale
window.resizable(height=FALSE, width=FALSE)

# kanvas untuk menampung semua widget
canvas = Canvas(window, width=500, height=400)
canvas.pack()

# gaya ttk untuk label
label_style = ttk.Style()
label_style.configure('TLabel', foreground='#191970', font=('OCR A Extended', 14))

# gaya ttk untuk tombol
button_style = ttk.Style()
button_style.configure('TButton', foreground='#191970', font=('DotumChe', 16))

# gaya ttk untuk entry
entry_style = ttk.Style()
entry_style.configure('TEntry', font=('Dotum', 15))

# label untuk menampilkan teks besar
big_label = Label(window, text='MENGHITUNG UMUR', foreground='#191970', font=('OCR A Extended', 25))

# Menempatkan label besar di dalam kanvas
canvas.create_window(245, 40, window=big_label)


# label dan entry untuk hari itu
day_label = ttk.Label(window, text='Tanggal:', style='TLabel')
day_entry = ttk.Entry(window, width=15, style='TEntry')

# label dan entry untuk bulan itu
month_label = ttk.Label(window, text='Bulan:', style='TLabel')
month_entry = ttk.Entry(window, width=15, style='TEntry')

# label dan entry untuk tahun ini
year_label = ttk.Label(window, text='Tahun:', style='TLabel')
year_entry = ttk.Entry(window, width=15, style='TEntry')

# tombol
calculate_button = ttk.Button(window, text='Menghitung Umur', style='TButton', command=calculate_age)

# label untuk menampilkan usia yang dihitung
age_result = ttk.Label(window, text='', style='TLabel')


# menambahkan label hari dan entry di dalam kanvas
canvas.create_window(114, 100, window=day_label)
canvas.create_window(130, 130, window=day_entry)

# menambahkan label bulan dan entry di dalam kanvas
canvas.create_window(250, 100, window=month_label)
canvas.create_window(245, 130, window=month_entry)

# menambahkan label tahun dan entry di dalam kanvas
canvas.create_window(350, 100, window=year_label)
canvas.create_window(360, 130, window=year_entry)

# menambahkan age_result dan entry di dalam kanvas
canvas.create_window(245, 180, window=age_result)

# menambahkan tombol hitung di dalam Koker
canvas.create_window(245, 220, window=calculate_button)


# menjalankan jendela tanpa batas hingga penggunaan menutupnya
window.mainloop()
