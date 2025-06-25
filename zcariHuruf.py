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
    kalimat = input("Kalimat: ")
    n = len(kalimat)
    simpan_huruf = [None] * n
    jumlah_huruf = [None] * n
    simpan = 0
    for i in range(n):
        if kalimat[i] != " ":
            sudah_ada = False
            for j in range(simpan):
                if simpan_huruf[j] == kalimat[i]:
                    jumlah_huruf[j] += 1
                    sudah_ada = True
            if not sudah_ada:
                simpan_huruf[simpan] = kalimat[i]
                jumlah_huruf[simpan] = 1
                simpan += 1
    for i in range(simpan):
        print(f"{simpan_huruf[i]}: {jumlah_huruf[i]}")

if __name__ == '__main__':
    main()
