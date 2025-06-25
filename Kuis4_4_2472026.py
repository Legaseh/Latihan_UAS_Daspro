# File : Kuis4_4_2472026.py s
# Penulis : Valentino Hose
# Tujuan Program : 

def matriks(d1,d2):
    arr = [None] * d1
    for i in range(0,d1,1):
        arr[i] = [None] *d2
    return arr
# Kamus Lokal:
# arr,N sebagai parameter untuk fungsi.
# for i: untuk mengakses tiap baris 
# for j: untuk mengakses tiap kolom 
def masukanMatriks(arr,N):
    for i in range(0,N,1):
        for j in range(0,N,1):
            arr[i][j]=int(input(""))
# Kamus Lokal:
# arr,N sebagai parameter untuk fungsi.
# for i: untuk mengakses tiap baris 
# for j: untuk mengakses tiap kolom 
def printMatriks(arr,N):
    for i in range(0,N,1):
        for j in range(0,N,1):
            print(arr[i][j], end=" ")
        print()
# Fungsi Utama:
# N:var, banyaknya data
# for i: untuk mengakses tiap indeks array
# data:array, untuk menyimpan semua data yang diinput
# dataUbah:array, untuk menyimpan semua data yang diubah
# h:var, untuk diagonal
# k:var sebagai indikaotor perubahan
# count:var menyimpan banyaknya data ganjil
# max : var, untuk menyimpan nilai terbesar dari matriks
def main():
    N = int(input("Ukuran matriks :"))
    data = matriks(N,N)
    dataUbah = matriks(N,N)
    masukanMatriks(data,N)
    print("Matriks mula-mula:")
    printMatriks(data,N)
    
    for j in range (0,N,1):
        k = 0 #sebagai indikator untuk perpindahan matriks
        
        for i in range (N-1,-1,-1):
            dataUbah[j][i] = data[k][j]
            k = k + 1
            
    print(f"Setelah diubah:")
    for i in range (0,N,1):
        for j in range (0,N,1):
            print(dataUbah[i][j],end=" ")
        print()
    count = 0
    max = 0
    for i in range(0,N,1):
        h = 2
        
        for j in range(0,N,1):
            if i == 0 or i == N-1:
                if (dataUbah[i][j]%2)==1 or dataUbah[i][h-i]%2 == 1:
                    count = count +1
                if (dataUbah[i][j] > max) or dataUbah[i][h-i] > max:
                    max = dataUbah[i][j]
 
            
    print(f"Bilangan ganjil pada huruf z ada: {count}")
    print(f"Bilangan terbesar pada huruf z:{max}")
    
    
if __name__ == '__main__':    
    main()   
