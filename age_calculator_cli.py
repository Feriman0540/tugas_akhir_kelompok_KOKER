from datetime import date

def calculate_age(day, month, year):
    #kami mendapatkan tanggal saat ini menggunakan date.today ()
    today = date.today()
    # mengubah tahun, bulan, dan hari menjadi tanggal lahir
    birthdate = date(year, month, day)
    # menghitung umur
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    # mengembalikan nilai umur
    return age


# Try/except
# percobaan akan dijalankan jika tidak ada pengecualian
try:
    # kita mendapatkan hari, bulan dan tahun menggunakan fungsi input()
    Tanggal = input('Tanggal:')
    Bulan = input('Bulan:')
    Tahun = input('Tahun:')
    # membuat variabel yang disebut calculate_age dan kami juga memanggil fungsi claculate_age
    age_result = calculate_age(int(Tanggal), int(Bulan), int(Tahun))
    print(f'Umur Kamu {age_result} Tahun')
    
# kecuali akan menangkap semua kesalahan
except:
    print(f'Gagal Menghitung Umur')