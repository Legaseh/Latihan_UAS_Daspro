# File : Kuis4_3_2472026.py
# Tujuan : program akan menampilkan nilai yang habis di bagi 3 dan 5
#   dan rata-rata nilai ganjil pada array

# Kamus Lokal:
# arr,N sebagai parameter untuk fungsi.
# for i: untuk mengakses tiap indeks array
def printHabisBagi35(arr,N):
    print("Bilangan yang habis di bagi 3 dan 5 :")
    for i in range(0,N,1):
        if (arr[i] % 3 ) == 0:
            if (arr[i] % 5) ==0:
                print(arr[i], end=" ")
    print()
# Kamus Lokal:
# arr,N sebagai parameter untuk fungsi.
# for i: untuk mengakses tiap indeks array
# Jumlah:var, untuk menyimpan jumlah nilai ganjil
# count:var, untuk menyimpan banyaknya data yang bisa dibagi 3 dan 5
def rataGanjil(arr,N):
    print("Rata-rata nilai ganjil pada array :")
    jumlah = 0
    count = 0
    for i in range(0,N,1):
        if (arr[i] % 2) == 1: 
            jumlah = jumlah + arr[i]
            count = count +1
    print(round((jumlah/count),2))

# Fungsi Utama:
# N:var, banyaknya data
# for i: untuk mengakses tiap indeks array
# data:array, untuk menyimpan semua data yang diinput
def main():
    N = int(input("N: "))
    data = [None] * N
    for i in range(0,N,1):
        data[i] = int(input("Data: "))
    printHabisBagi35(data,N)
    rataGanjil(data,N)
        
if __name__ == '__main__':    
    main()   