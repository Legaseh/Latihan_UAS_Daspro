# #soal 3
# def isiArray(n):
#     data = [None] * n
#     for i in range(0,n,1):
#         data[i] = int(input(""))
#     return data

# def printArray(n,arr):
#     for i in range(0,n,1):
#         print(arr[i],end=" ")
#     print()

# def urutin(n,arr):
#     for p in range(0,n,1):
#         imin = p
#         for i in range(p+1,n,1):
#             if arr[i] < arr[imin] :
#                 imin = i
#                 print(f"{arr[i]} lebih kecil dari {arr[imin]}")
#         temp = arr[p]
#         arr[p] = arr[imin]
#         arr[imin] = temp
        
# def main():
#     n = int(input("N: "))
#     arr = isiArray(n)
#     print("Array mula-mula: ",end="")
#     printArray(n,arr)
#     urutin(n,arr)
#     printArray(n,arr)
    
    
    
# if __name__ == '__main__':
#     main()
    
    
#soal 4

def matriks(d1,d2):
    arr = [None]*d1
    for i in range(0,d1,1):
        arr[i] = [None]*d2
    return arr 

def isiMatriks(n,data):
    for i in range(0,n,1):
        for j in range(0,n,1):
            data[i][j] = int(input(""))

def printArray(n,data):
    for i in range(0,n,1):
        for j in range(0,n,1):
            print(data[i][j],end=" ")
        print()

def hitung (n,data,data1):
    print("Hasil penjumlahan matriks (A + B) :")
    for i in range(0,n,1):
        for j in range(0,n,1):
            h = data[i][j] + data1[i][j]
            print(h,end=" ")
        print()
    print()
    print("Hasil penjumlahan matriks (A - B) :")
    for i in range(0,n,1):
        for j in range(0,n,1):
            h = data[i][j] - data1[i][j]
            print(h,end=" ")
        print()

def main():
    n = int(input("N: "))
    print("Masukkan elemen-elemen matriks A: ")
    A = matriks(n,n)
    isiMatriks(n,A)
    print()
    print("Masukkan elemen-elemen matriks B: ")
    B = matriks(n,n)
    isiMatriks(n,B)
    print()
    print("Matriks A: ")
    printArray(n,A)
    print()
    print("Matriks B: ")
    printArray(n,B)
    print()
    
    hitung(n,A,B)
if __name__ == '__main__':
    main()