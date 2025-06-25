
def matriks(d1,d2):
    arr = [None]*d1
    for i in range(0,d1,1):
        arr[i] = [None]*d2
    return arr

def isiMatrisk (n,data):
    for i in range(n):
        for j in range(n):
            data[i][j] = int(input(f"Matriks {i},{j}: "))
    print()
    return

def printArray(n,data):
    for i in range(n):
        for j in range(n):
            print(data[i][j],end=" ")
        print()
    return

def hitung(n,data,data1,indi):
    for i in range(n):
        for j in range(n):
            if indi == "+":
                data[i][j] = data[i][j] + data1[i][j]
            elif indi == "-":
                data[i][j] = data[i][j] - data1[i][j]
            else:
                print("Operasi Tidak Tersedia")
    return data

def main ():
    n = int (input("Matriks: "))
    data = matriks(n,n)
    dataPerbandingan = matriks(n,n)
    
    print("Matriks H")
    isiMatrisk(n,data)
    
    print("Matriks I")
    isiMatrisk(n,dataPerbandingan)
    
    nanya = str(input("Operasi (+/-): "))
    print()
    print("Matriks H")
    printArray(n,data)
    print(nanya)
    print("Matriks I")
    printArray(n,dataPerbandingan)
    
    x = (hitung(n,data,dataPerbandingan,nanya))
    print()
    printArray(n,x)

if __name__ == "__main__" :
    main()