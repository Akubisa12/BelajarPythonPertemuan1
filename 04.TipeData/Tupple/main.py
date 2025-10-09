"""
Tuple di PythonPengertian TupleTuple adalah struktur data di Python yang menyimpan koleksi item terurut dan immutable (tidak dapat diubah). Karakteristik tuple:

    1. Ordered (memiliki urutan/index)
    2. Immutable (tidak dapat diubah setelah dibuat)
    3. Mengizinkan duplikasi (elemen boleh sama)
    4. Dapat berisi berbagai tipe data
    5. Menggunakan tanda kurung () atau tanpa kurung
    6. Lebih cepat dan hemat memori dibanding list
"""
# A. Membuat Tuple
# Tuple kosong
tuple_kosong = ()
tuple_kosong2 = tuple()

# Tuple dengan data
angka = (1, 2, 3, 4, 5)
buah = ("apel", "jeruk", "mangga")

# Tuple tanpa kurung (tuple packing)
koordinat = 10, 20, 30
print(type(koordinat))  # Output: <class 'tuple'>

# Tuple dengan satu elemen (HARUS ada koma)
satu_elemen = (5,)  # Benar
bukan_tuple = (5)   # Salah! Ini integer, bukan tuple
print(type(satu_elemen))  # Output: <class 'tuple'>
print(type(bukan_tuple))  # Output: <class 'int'>

# Tuple dengan berbagai tipe data
campuran = (1, "dua", 3.0, True, [4, 5])

# Membuat tuple dari list/string
tuple_dari_list = tuple([1, 2, 3])
tuple_dari_string = tuple("hello")
print(tuple_dari_string)  # Output: ('h', 'e', 'l', 'l', 'o')


# B. Mengakses elemen dengan tuple
# buah = ("apel", "jeruk", "mangga", "pisang", "anggur")

# Akses dengan index (dimulai dari 0)
# print(buah[0])   # Output: apel
# print(buah[2])   # Output: mangga

# Akses dengan index negatif (dari belakang)
# print(buah[-1])  # Output: anggur
# print(buah[-2])  # Output: pisang

# Slicing
# print(buah[1:4])   # Output: ('jeruk', 'mangga', 'pisang')
# print(buah[:3])    # Output: ('apel', 'jeruk', 'mangga')
# print(buah[2:])    # Output: ('mangga', 'pisang', 'anggur')
# print(buah[::2])   # Output: ('apel', 'mangga', 'anggur')
# print(buah[::-1])  # Output: tuple terbalik

# Index out of range akan error
# print(buah[10])  # IndexError

# C. Operasi di dalam Tuple
# tuple1 = (1, 2, 3)
# tuple2 = (4, 5, 6)

# Concatenation (penggabungan)
# gabungan = tuple1 + tuple2
# print(gabungan)  # Output: (1, 2, 3, 4, 5, 6)

# Repetition (pengulangan)
# ulang = tuple1 * 3
# print(ulang)  # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)

# Membership (in/not in)
# print(2 in tuple1)      # Output: True
# print(10 not in tuple1) # Output: True

# Length
# print(len(tuple1))  # Output: 3

# D. Built in Function di tuple (fungsi bawaan di tuple)
# angka = (5, 2, 8, 1, 9, 3)

# min() - nilai minimum
# print(min(angka))  # Output: 1

# max() - nilai maksimum
# print(max(angka))  # Output: 9

# sum() - jumlah total
# print(sum(angka))  # Output: 28

# sorted() - return list terurut (tidak mengubah tuple)
# terurut = sorted(angka)
# print(terurut)  # Output: [1, 2, 3, 5, 8, 9]
# print(type(terurut))  # Output: <class 'list'>

# any() - True jika ada elemen yang True
# print(any((0, False, True)))  # Output: True

# all() - True jika semua elemen True
# print(all((1, 2, 3)))  # Output: True