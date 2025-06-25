def isiArray ():
    global data 
    n = int(input("N: "))
    for i in range(0,n):
        data[i] = int(input("Data: "))
    return n

def printArray(n):
    global data
    for i in range(0,n):
        print(data[i])

def ngurutin(n): #nilai tertinggi atau terendah
    global data
    for p in range(0,n-1): #ngambil data pertama banget
        imin = p #indeks nilai terbesar/terkecil
        for i in range(p+1,n): #ngambil data kedua
            if (data[i] < data[imin]): # pengecekan mau yang terbesar/terkecil
                imin = i #menyimpan data terbesar/terkecil yang baru
        temp = data[p]
        data[p] = data[imin]
        data[imin] = temp
    return

def SortedSearch(N,cari):
    Found = False
    atas = 0 #batas paling awal
    bawah  = N-1 #batas paling akhir
    ix = -1 #hasilnya nemu/tidak
    while (atas <= bawah and not Found): #ini tuh jalan kalau bener
        tengah = (atas + bawah)//2
        if (data[tengah] == cari):
            Found = True
            ix = tengah
        elif (cari < data[tengah]):
            bawah = tengah-1
        else:
            atas = tengah + 1
    return ix
    
def bubble_sort(n): #pake cara bubble sort.
    global data
    for i in range(n):
        for j in range(0, n - 1 - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]

def insertion_sort_trace(n): 
    global data
    for i in range(1, n):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key: #ketika j lebih besar== 0 dan data[j] lebih besar dari key baru di jalanin.
            #ini tuh buat ngecek tiap indeks kalau ada yang paling besarnya gitu lah.
            data[j + 1] = data[j]
            j -= 1 #ini buat perpindahan ke kirinya maksdunya index nya tuh makin kecil gt.

        data[j + 1] = key #nah setelah segala cek di while di sini baru di ubah si keynya di simpan yang di ceknya gt.

def main ():
    n = isiArray()
    insertion_sort_trace(n)
    printArray(n)

if __name__ == "__main__" :
    data = [None] * 100
    main()