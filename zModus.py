# File : T11A_2472026.py 
# Penulis : Valentino Hose
# Tujuan Program : 
# Kamus data

def nilaiTengah(arr,n):
    max = 0
    min = 99
    for i in range (0,n,1):
        if arr[i] > max:
            max = arr[i]
        if arr[i] < min:
            min = arr[i]
    nTengah = (min + max)//2
    return nTengah

# ini blm
def nilaiModus(arr,n):
    Angka = [None] * n
    Frek = [0] * n
    h = 0
    for i in range (0,n,1):
        cek = False
        for j in range(0,i,1):
            if arr[i] == Frek[j]:
                cek = True
        if cek == False :
            Angka[h] = arr[i]
            Frek[h] += 1
            h += 1
    max = 0
    imax = 0
    for i in range (0,h,1):
        if Frek[i] > imax:
            imax = Frek[i]
            max = Angka[i]
    return max
                

def main():
    n = int(input("N :"))
    data = [None] * n
    for i in range (0,n,1):
        data[i] = int(input(f"Masukan angka ke-{i+1}: "))
    print("Nilai tengah: ",nilaiTengah(data,n))
    print("Modus:",nilaiModus(data,n))
if __name__ == '__main__':    
    main()   
