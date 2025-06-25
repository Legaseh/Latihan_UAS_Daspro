# File : T09C_2472026.py 
# Penulis : Valentino Hose
# Tujuan Program : Menampilkan jumlah bilangan ganjil pada
#   indeks genap dan jumlah bilangan genap pada ideks ganjil.
# Kamus data
# NMAX : batas maksimum yang dapat diinput ke array (integer)
# count : menghitung ada berapa si data yang diinput (integer)
# jum_genap : menyimpan jumlah nilai genap pada indeks ganjil (integer)
# jum_ganjil : menyimpan jumlah nilai ganjil pada indeks genap (integer)
# A : menyimpan data yang diinputkan (array-integer)
# data : nilai yang ingin di cek (integer)
# for i : untuk mengulang tiap indeks dari array (integer)
def main():
    print ("Silahkan memasukan bilangan")
    NMAX = 100
    count = 0
    jum_genap = 0
    jum_ganjil = 0
    A = [None] * NMAX
    data = int(input(""))
    while (data != 999):
        A[count] = data
        count = count +1
        data = int(input(""))
    print ("Isi aray:")
    for i in range (0,count,1):
        print (f"Arr[{i}]:{A[i]}")
        if ((i%2)==0):
            if ((A[i]%2) == 1):
                jum_ganjil = jum_ganjil + A[i]
        else:
            if ((A[i]%2) == 0):
                jum_genap = jum_genap + A[i]
            
    print (f"Jumlah bilangan ganjil pada indeks genap: {jum_ganjil}")
    print (f"Jumlah bilangan genap pada indeks ganjil: {jum_genap}")
if __name__ == '__main__':    
    main()   