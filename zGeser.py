# File : T09D_2472026.py 
# Penulis : Valentino Hose
# Tujuan Program : Menampilkan geser bilangan dai kondisi awal
# kamus data
# n : sebagai indikator berapa banyak isi array (integer)
# A : sebagai array menyimpan data (integer)
# for i : untuk mengakses tiap array nya (integer)
# geser : untuk menentukan pergeserannya mau berapa (integer)
# simpan_geser : menyimpan hasil dari nilai yang di geser (integer)

def main():
    n = 10
    A = [None] * 10
    for i in range (0,n,1):
        A[i] = int(input(""))
    geser = int(input("Jumlah pergeseran :"))
    print (f"Kondisi awal:{A}")
    simpan_geser = A[n-geser:n]
    print(simpan_geser)
    for i in range (n-1,-1,-1):
        print(i)
        A[i] = A[i-geser]
    A[0:geser] = simpan_geser
    print (f"Setelah pergeseran:{A}")
    
if __name__ == '__main__':    
    main()   
