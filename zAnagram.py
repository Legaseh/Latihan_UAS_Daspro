# File : T11B_2472026.py 
# Penulis : Valentino Hose
# Tujuan Program : 
# Kamus data

def checkAnagram(str1,str2):
    print (str1)
    print (str2)
    
def main():
    n = int (input(""))
    kata1 = [None] * 10
    kata2 = [None] * 10
    for i in range (0,n,1):
        kata1[i] = str(input(""))
    for i in range (0,n,1):
        kata2[i] = str(input(""))
    for i in range (0,n,1):
        if len(kata1[i]) == len(kata2[i]):
            print (f"Anagram: {kata1[i]} {kata2[i]}")
        else:
            # hrsnya di cek ke fungsi baru di print dari hasil 
            # fungsinya
            print(f"Bukan anagram: {kata1[i]} {kata2[i]}")
    
    
if __name__ == '__main__':    
    main()   
