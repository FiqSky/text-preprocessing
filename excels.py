import xlsxwriter

workbook = xlsxwriter.Workbook('arrays.xlsx')
worksheet = workbook.add_worksheet()

array = [["nama", "tuban", "jawa", "timur", "populer", "telinga", "traveler", "namun", "air", "terjun", "ngilip", "singgah", "asri", "air", "terjun", "nglirip", "camat", "singgah", "tuban", "kenal", "kalang", "ajar", "anak", "muda", "tuban", "kali", "sempat", "pergi", "nglirip", "biasa", "kali", "pulang", "kampung", "tuju", "utama", "jalan", "jalan", "pantai", "namun", "momen", "libur", "raya", 2017, "ajak", "tim", "ntuk", "coba", "jalan", "jalan", "pantai", "jalan", "lokasi", "air", "terjun", "nglirip", "rumah", "ngimbang", "palang", 54, "km", "38km", "kota", "tuban", "rute", "kota", "tuban", "camat", "montong", "camat", "singgah", "jalan", "rute", "senang", "jalan", "relatif", "mulus", "pandang", "enak", "pandang", "lok", "ekstrim", "sampai", "lokasi", "bingung", "parkir", "lahan", "parkir", "telah", "pas", "gerbang", "masuk", "parkir", "mobil", "persis", "seberang", "jalan", "melaui", "jalan", "batu", "sempit", "lumayan", "luas", "parkir", "puluh", "mobil", "pintu", "masuk", "lokasi", "air", "terjun", "sisi", "atas", "air", "terjun", "beli", "karcis", "harga", "rp", 10, "ribu", "dewasa", "rp", 8, "ribu", "anak", "anak", "kemudian", "turun", "jalan", "curam", "periksa", "karcis", "turun", "palu", "anak", "tangga", "semen", "dasar", "air", "terjun", "di", "orang", "orang", "main", "air", "tuju", "main", "air", "lihat", "telah", "puas", "nikmat", "air", "terjun", "ambil", "foto", "parkir", "lokasi", "main", "air", "lokasi", "air", "terjun", "jalan", "masuk", "lokasi", "sumber", "mata", "air", "tuju", "renang", "sembunyi", "orang", "tahu", "letak", "belah", "kanan", "jalan", "lokasi", "air", "terjun", "tanda", "turun", "curam", "tau", "bawa", "mobil", "parkir", "di", "sumber", "mata", "air", "nikmat", "segar", "renang", "sungai", "air", "sisi", "sisi", "sungai", "telah", "puas", "renang", "nikmat", "segar", "air", "sungai", "jernih", "perih", "mata", "kolam", "renang", "sholat", "dzuhur", "mushola", "sedia", "parkir", "pulang", "di", "sedia", "toilet", "kawatir", "hal", "pantai", "pasir", "putih", "remen", "toilet", "lah", "jalan", "jalan", "lupa", "makan", "bareng", "rekomendasi", "tim", "kali", "makan", "mie", "ayam", "kota", "tuban", "tepat", "arah", "empat", "patung", "arah", "terminal", "belah", "kiri", "jalan", "mie", "nya", "lumayan", "enak", "harga", "rp", "10", "ribu", "layak", "coba", "sempat"]]

row = 0

for col, data in enumerate(array):
    worksheet.write_column(row, col, data)

workbook.close()
