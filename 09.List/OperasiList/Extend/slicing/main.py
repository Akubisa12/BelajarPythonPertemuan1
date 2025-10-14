#membuat list_1
list_1 = [10,70,20]
# membuat list_2
list_2 = [68, 77]
# len(list_1) akan menghasilkan 3 
""" 
list_1[3:] akan memilih semua elemen di akhir karena list_1 hanya memiliki indeks 0,1,dan 2, maka indeks ke-3 adalah posisi tepat diakhir list.
Setelah itu baru kita masukkan ke variabel list_2
"""
list_1[len(list_1):] = list_2
# cetak isi dari list_1
print(list_1)

#memubat list
list_1 = [10,70,20]
list_2 = [88,77]
# operator + pada list berfungsi untuk konkatenasi(penggabungan). Operasi ini akan membuat sebuah list baru yang berisi semua elemen dari list_1 oleh semua elemen dari list_2 dan kemudian disimpan ke dalam variabel list_3
list_3 = list_1 + list_2
# mencetak list_3
print(list_3)