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

def sort(n):
    global data
    for p in range(0,n,1):
        imin = p 
        for i in range(p+1,n,1):
            if data[i] < data[imin]:
                imin = i
        temp = data[p]
        data[p] = data[imin]
        data[imin] = temp
    return data

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
    
def main ():
    n = isiArray()
    sort(n)
    x = int(input("Mau cari angka berapa: "))
    SortedSearch(n,x)
    printArray(n)

if __name__ == "__main__" :
    data = [None] * 100
    main()