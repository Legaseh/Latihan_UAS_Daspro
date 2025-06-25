# File : T11D_2472026.py 
# Penulis : Valentino Hose
# Tujuan Program : menampilkan hasil dari nama dan ipk, serta
#   rata-rata ipk lalu ipk terendah dan tertinggi.

# Kamus Lokal
# arr,ipk,n : sebagai parameter untuk fungsi cetakArray
#   (integer dan string)
# for i : untuk mengakses tiap indeks dari array (integer)
def cetakArray(arr,ipk,n):
    print ("Nama IPK:")
    for i in range (0,n,1):
        print(f"{arr[i]} {ipk[i]}")

# Kamus Lokal
# arr,n : sebagai parameter untuk fungsi rataRata(integer)
# for i : untuk mengakses tiap indeks dari array (integer)
# jumlah : var, untuk menyimpan hasil jumlah ipk (integer)
def rataRata (arr,n):
    jumlah = 0
    for i in range (0,n,1):
        jumlah = arr[i] + jumlah
    return jumlah/n

# Kamus Lokal
# arr,n : sebagai parameter untuk fungsi nilaiMaksimum(integer)
# for i : untuk mengakses tiap indeks dari array (integer)
# max : var, untuk menyimpan indeks ipk terbesar (integer)
def nilaiMaksimum(arr,n):
    max = 0
    for i in range (0,n,1):
        if (arr[i] > arr[max]):
            max = i
    return max
# Kamus Lokal
# arr,n : sebagai parameter untuk fungsi nilaiMinimum(integer)
# for i : untuk mengakses tiap indeks dari array (integer)
# min : var, untuk menyimpan indeks ipk terkecil (integer)
def nilaiMinimum(arr,n):
    min = 0
    for i in range (0,n,1):
        if (arr[i] < arr[min]):
            min = i
    return min

# Program Utama
# Kamus data
# N : var, untuk input ada berapa data yang akan diinput (integer)
# nama : var, untuk menyimpan nama yang diinput (string)
# ipk : var, untuk menyimpan ipk yang diinput (integer)
# for i : loop, untuk mengakses dari setiap indeks pada array(integer)
# hasilMin : var, menyimpan hasil nilai terendah dari data (integer)
# hasilMax : var, menyimpan hasil nilai tertinggi dari data (integer)
def main():
    N = int(input(""))
    nama = [None] * N
    ipk = [None] * N
    for i in range (0,N,1):
        nama[i] = str(input(""))
    for i in range (0,N,1):
        ipk[i] = float(input(""))
    cetakArray(nama,ipk,N)
    print ("IPK rata-rata", '{0:4.2f}'.format(rataRata(ipk,N)))
    print ("IPK rata-rata", round((rataRata(ipk,N)),2))
    hasilMin = nilaiMinimum(ipk,N)
    print ("IPK Terendah:",nama[hasilMin],"-", ipk[hasilMin])
    hasilMax = nilaiMaksimum(ipk,N)
    print ("IPK Tertinggi:",nama[hasilMax],"-", ipk[hasilMax])
if __name__ == '__main__':    
    main()   


