# Tujuan: Baris jadi Kolom dari 2x3
def matriks(d1,d2):
    arr = [None]*d1
    for i in range(0,d1,1):
        arr[i] = [None]*d2
    return arr

def isiMatriks(data):
    for i in range(0,3,1):
        for j in range(0,2,1):
            data[i][j] = int(input(f"Isi untuk {i} {j}: "))

def ubahMatriks(data,ubahdata):
    for i in range(0,3,1): # 0 1 2
        for j in range(0,2,1): # 0 1
            ubahdata[j][i] = data[i][j]


def printMatriks(ubahdata):
    for i in range(0,2,1):
        for j in range(0,3,1):
            print(ubahdata[i][j],end=" ")
        print()
def main():
    data = matriks(3,2)
    ubahdata = matriks(2,3)
    isiMatriks(data)
    ubahMatriks(data,ubahdata)
    printMatriks(ubahdata)
  
if __name__ == "__main__":
    main()
    
# 2 3
# 4 3
# 4 5

# jadi
# 2 4 4
# 3 3 5