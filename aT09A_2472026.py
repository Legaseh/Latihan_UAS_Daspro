# File : T09A_2472026.py 
# Penulis : Valentino Hose
# Tujuan Program : Menampilkan jumlah bilangan, bilangan terbesar,
#   dan terkecil pada indeksnya.
# Kamus data
# n : banyaknya data yang akan di input (integer)
# total : menyimpan jumlah data yang diinput (integer)
# imax : menyimpan indeks ke berapa nilai terbesar (integer)
# max : menyimpan nilai terbesar (integer)
# imin : menyimpan indeks ke berapa nilai terkecil (integer)
# min : menyimpan nilai terkecil (integer)
# A : array untuk menyimpan keseluruhan data (array-integer)
# for i : untuk menyimpan ke array A dan untuk mengecek
#   terbesar dan terkecil (integer)

def main():
    n = 10
    total = 0
    imax = 0
    max = 0
    imin = 0
    min = 999
    A = [None] * n
    for i in range (0,n,1):
        data = int(input(f"Arr[{i}]:"))
        A[i] = data
        total = total + data
    for i in range (0,n,1):
        if A[i] > max :
            max = A[i]
            imax = i
        if A[i] < min :
            min = A[i]
            imin = i
    print (f"Jumlah bilangan:{total}")
    print (f"Bilangan terbesar berada pada indeks {imax}")
    print (f"Bilangan terkecil berada pada indeks {imin}")
    
if __name__ == '__main__':    
    main()   
