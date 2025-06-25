# File : T09E_2472026.py 
# Penulis : Valentino Hose
# Tujuan Program : menampilkan hasil huruf vokal dan konsonan.
# Kamus data
# kalimat : sebagai array dari kalimat yang diinput (array-string)
# vokal : untuk menyimpan jumlah huruf vokal (integer)
# konsonan : untuk menyimpan jumlah huruf konsonan (integer)
# n : menyimpan jumlah panjang kalimatnya (integer)
# for i : untuk mengakses tiap indeks dari array (integer)
def main():
    kalimat = str(input("Kalimat: "))
    vokal = 0
    konsonan = 0
    n = len(kalimat)
    for i in range (n):
        if (kalimat[i] == "a") or (kalimat[i] == "i") or (kalimat[i] == "u") or (kalimat[i] == "e") or (kalimat[i] == "o"):
            vokal = vokal + 1
        else:
            if (kalimat[i] != " " ) and (kalimat[i] != "."):
                konsonan = konsonan + 1
    print (kalimat)
    print (f"Jumlah huruf vokal: {vokal} hururf")
    print (f"Jumlah huruf konsonan: {konsonan} hururf")
if __name__ == '__main__':    
    main()   
