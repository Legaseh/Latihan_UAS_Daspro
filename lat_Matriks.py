def isiArray ():
    global n
    for i in range(0,n):
        for j in range(0,n):
            data[i][j] = int(input(f"Matriks {i}:{j}: "))

def main ():
    isiArray()

if __name__ == "__main__" :
    n = int(input("brp x brp? "))
    data = [None] * n
    for i in range(n):
        data[i] = [None] * n
    main()