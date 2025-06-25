# File : Kuis4_2_2472026.py 
# Penulis : Valentino Hose
# Tujuan Program : Memperbaiki kesalahan (Program akan menampilkan
#   indeks dari data yang dicari atau menampilkan bahwa data tidak
#   terdaftar).

#Fungsi Cari(N,X)
#mencari X dalam array Data
#N : banyaknya data dalam array(integer)
#X : nilai yang dicari (integer)
#A : array [1..N]of integer
#fungsi mengirimkan indeks
#Jika X ditemukan,fungsi mengirim nilai i dlm indeks
#jika X tidak ditemukan, fungsi mengirim -1 dlm indeks
def Cari(N,X):
    global A #n = 8
    i = 0
    while (A[i] != X) and (i < N):
        i = i + 1
    if (A[i] == X):
        indeks = i
    else:
        indeks = -1
    return indeks


def main():
    global A
    N = 8
    for i in range(0,N,1):
        A[i] = int(input("nilai:"))
    info = int(input("info yang dicari:"))
    p = Cari(N,info)
    if (p >= 0):
        print(info,"ada di posisi ",p)
    else:
        print(info,"tidak terdaftar")
    
if __name__ == '__main__':    
    Nmax = 10
    A = Nmax * [None]
    main()   
