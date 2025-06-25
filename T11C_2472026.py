# File : T11C_2472026.py 
# Penulis : Valentino Hose
# Tujuan Program : yang koma koma itu lah
# Kamus data

def masukinArray(n):
    data = [None] * n
    for i in range(0,n,1):
        data[i] = str(input(f"Masukan Kalimat ke-{i+1}: "))
    return data

def cekKata(n,data):
    for i in range(0,n,1):
        count = 0
        kalimat = data[i]
        koma = ""
        for h in range(0,len(kalimat),1):
            if kalimat[h] == " ":
                koma = koma + ", "
                count = count + 1
            else:
                koma = koma+kalimat[h]
        print(koma,count+1)

def main():
    n = int(input("N : "))
    arr = masukinArray(n)
    print(arr)
    cekKata(n,arr)

if __name__ == '__main__':
    main()