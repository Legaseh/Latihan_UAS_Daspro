# File : T09F_2472026.py 
# Penulis : Valentino Hose
# Tujuan Program : mengecek apakah kata tersebut polindrom atau bukan
# Kamus data
# kata : untuk menyimpan data inputan (array-string)
# benar : menentukan apakah kata tersebut polindrom atau bukan (integer)
# n : untuk menghasilkan panjang dari kata yang diinput (integer)
# for i : mengecek setiap indeks dari array katanya (integer)
def main():
    kata = str(input("Kata:"))
    benar = 0
    n = len(kata)
    for i in range (0,n,1):
        if (kata[i]) == kata[n-i-1]:
            benar = benar + 1
    if benar == n:
        print (f"{kata} merupakan kata polindrom")
    else:
        print (f"{kata} bukan merupakan kata polindrom")
if __name__ == '__main__':    
    main()   
