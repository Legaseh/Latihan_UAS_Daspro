# File : T09B_2472026.py 
# Penulis : Valentino Hose
# Tujuan Program : menampilkan hasil reverse dari array
# Kamus data
# n: untuk akan ada berapa data yang diinput (integer)
# A: menyimpan data sebanyak n (array - integer)
# reverse : menyimpan data yang telah di reverse (string)
# data : untuk menyimpan inputan bilangan (integer)
# for i ; untuk mengakses tiap array (integer)
def main():
    n = int(input("Berapa banyak bilangan yang akan dimasukan?"))
    A = [None] * n
    reverse = ""
    for i in range (0,n,1):
        A[i] = int(input(f"Bil ke-{i}: "))
    print (f"Array awal: {A}")
    for i in range (n-1,-1,-1):
        if (i == 0):
            reverse = reverse + str(A[i])
        else:
            reverse = reverse + str(A[i]) +", "
            
    print (f"Array reverse: [{reverse}]")
    
if __name__ == '__main__':    
    main()   
