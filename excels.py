import xlsxwriter

workbook = xlsxwriter.Workbook('arrays.xlsx')
worksheet = workbook.add_worksheet()

array = [['Secara', 'administratif', 'Air', 'Terjun', 'Nglirip', 'Tuban', 'terletak', 'Dusun', 'Jojogan', 'Desa', 'Mulyo', 'Agung', 'Kecamatan', 'Singgahan', 'Jarak', 'Dari', 'Pusat', 'Kota', 'Tuban', 'terhitung', '37', 'Km', 'arah', 'barat', 'daya', 'Menuju', 'air', 'terjun', 'ditempuh', 'kendaraan', 'pribadi', 'kendaraan']]

row = 0

for col, data in enumerate(array):
    worksheet.write_column(row, col, data)

workbook.close()
