def insertion_sort_trace(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        print(key)
        print(i,"ini i")
        print(j, "j awal")
        while j >= 0 and arr[j] > key: #ketika j lebih besar == 0 dan arr[j] lebih besar dari key baru di jalanin.
            #ini tuh buat ngecek tiap indeks kalau ada yang paling besarnya gitu lah.
            arr[j + 1] = arr[j]
            j -= 1 #ini buat perpindahan ke kirinya maksdunya index nya tuh makin kecil gt.

        arr[j + 1] = key #nah setelah segala cek di while di sini baru di ubah si keynya di simpan yang di ceknya gt.
        print(f"Langkah {i}: {arr}")  # Menampilkan array setiap langkah

insertion_sort_trace([7, 3, 5, 2,1,8,3])
