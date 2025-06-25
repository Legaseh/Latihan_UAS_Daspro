# File : T09H_2472026.py 
# Penulis : Valentino Hose
# Tujuan Program : menampilkan nilai dengan nama siswa untuk nilai tertinggi
#   dan siswa yang memiliki nilai diatas nilai rata-rata.
# Kamus data
# nilai : sebagai array untuk nilai siswa (array-integer)
# nama : sebagai array untuk nama siswa (array-string)
# max : untuk menyimpan data nilai terbesar (integer)
# jumlah : menyimpan hasil jumlah nilai keseluruhan siswa (integer)
# for i : untuk mengakses tiap indeks dari array (integer)
# imax : untuk menyimpan indesknya (integer)
def main():
    nilai = [None] * 10
    nama = [None] * 10
    max = 0
    jumlah = 0
    for i in range (0,10,1):
        nama[i] = str(input(f"Nama Siswa {i+1}:"))
        nilai[i] = int(input(f"Nilai Siswa {i+1}:"))
        print ("-"*27)
    for i in range (0,10,1):
        if nilai[i] >= max:
            max = nilai[i]
            imax = i
        jumlah = jumlah + nilai[i]
    print (f"Siswa dengan nilai tertinggi diperoleh oleh {nama[imax]} dengan nilai {nilai[imax]}")
    print (f"Nilai rata-rata: {jumlah/10}")
    print (f"Daftar siswa dengan nilai diatas nilai rata-rata:")
    for i in range (0,10,1):
        if nilai[i]> (jumlah/10):
            print (f"{nama[i]} {nilai[i]}")
if __name__ == '__main__':    
    main()   
