def Matriks(d1,d2):
    data = [None] * d1    
    for i in range(0,d1,1):
        data[i] = [None] * d2
    return data  

def isiMatriks (n,data):
    for i in range(0,n,1):
        for j in range(0,n,1):
            data[i][j] = int(input(""))
    return

def printMatriks(n,data):
    for i in range(0,n,1):
        for j in range(0,n,1):
            print(data[i][j],end=" ")
        print()

def flat(n,data):
    index = 0
    d = [None] * (n*n)
    for i in range(0,n,1):
        for j in range(0,n,1):
            d[index] = data[i][j]
            index = index + 1
    return d

def sort(n,data):
    for p in range(0,n*n,1):
        imin = p 
        for i in range(p+1,n*n,1):
            if data[i]< data[imin]:
                imin = i
        temp = data[p]
        data[p] = data[imin]
        data[imin] = temp
    return data

def SortedSearch2D(data, cari):
    rows = len(data)
    cols = len(data[0])
    print (rows)
    print (cols)
    kiri = 0
    kanan = rows * cols - 1

    while kiri <= kanan:
        mid = (kiri + kanan) // 2
        # Konversi indeks 1D ke 2D
        i = mid // cols
        j = mid % cols

        if data[i][j] == cari:
            return (i, j)
        elif cari < data[i][j]:
            kanan = mid - 1
        else:
            kiri = mid + 1

    return None  # Tidak ditemukan


def main():
    n = int(input("N : "))
    arr = Matriks(n,n)
    isiMatriks(n,arr)
    printMatriks(n,arr)

    dimensi_1 = flat(n,arr)
    print(dimensi_1)
    a = sort(n,dimensi_1)
    for i in range(0,n*n,1):
        print(a[i],end=" ")
    print()
    
    index = 0
    for i in range(0,n,1):
        for j in range(0,n,1):
            arr[i][j] = a[index]
            index = index + 1
            
    printMatriks(n,arr)
    print(SortedSearch2D(arr,3))
    
    
    
    
if __name__ == '__main__':
    main()