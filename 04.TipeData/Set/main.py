"""
Pengertian SetSet adalah struktur data di Python yang menyimpan koleksi item unik dan tidak berurutan. Karakteristik set:

    A. Unordered (tidak memiliki urutan/index)
    B. Mutable (dapat diubah)
    C. Tidak mengizinkan duplikasi (setiap elemen harus unik)
    D. Elemen harus immutable (string, number, tuple)
"""

# A. Membuat Set 
# Set kosong - HARUS menggunakan set()
set_kosong = set()  # Benar
# set_kosong = {}   # Salah! Ini akan membuat dictionary

# Set dengan data
angka = {1, 2, 3, 4, 5}
buah = {"apel", "jeruk", "mangga"}

# Membuat set dari list (menghilangkan duplikat)
list_angka = [1, 2, 2, 3, 3, 3, 4]
set_angka = set(list_angka)
print(set_angka)  # Output: {1, 2, 3, 4}

# Set dari string
huruf = set("hello")
print(huruf)  # Output: {'h', 'e', 'l', 'o'}

# Set dengan tipe data campuran
campuran = {1, "dua", 3.0, (4, 5)}

# B. Menambah dan menghapus elemen di dalam set
# buah = {"apel", "jeruk"}

# Menambah satu elemen
# buah.add("mangga")
# print(buah)  # Output: {'apel', 'jeruk', 'mangga'}

# Menambah multiple elemen
# buah.update(["pisang", "anggur"])
# buah.update({"melon", "semangka"})

# Menghapus elemen - error jika tidak ada
# buah.remove("apel")  # Error jika 'apel' tidak ada

# Menghapus elemen - tidak error jika tidak ada
# buah.discard("durian")  # Aman, tidak error

# Menghapus dan return elemen random
# item = buah.pop()
# print(item)

# Menghapus semua elemen
# buah.clear()

# C. Operasi didalam Set
# A = {1, 2, 3, 4, 5}
# B = {4, 5, 6, 7, 8}

# 1. UNION (Gabungan) - semua elemen dari kedua set
# print(A | B)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}
# print(A.union(B))

# 2. INTERSECTION (Irisan) - elemen yang ada di kedua set
# print(A & B)  # Output: {4, 5}
# print(A.intersection(B))

# 3. DIFFERENCE (Selisih) - elemen di A tapi tidak di B
# print(A - B)  # Output: {1, 2, 3}
# print(A.difference(B))

# 4. SYMMETRIC DIFFERENCE - elemen di A atau B tapi tidak keduanya
# print(A ^ B)  # Output: {1, 2, 3, 6, 7, 8}
# print(A.symmetric_difference(B))


# D. Method penting didalam Set
# angka = {1, 2, 3, 4, 5}

# len() - jumlah elemen
# print(len(angka))  # Output: 5

# in - mengecek keberadaan elemen
# print(3 in angka)  # Output: True
# print(10 in angka)  # Output: False

# copy() - membuat salinan
# salinan = angka.copy()

# issubset() - mengecek apakah subset
# A = {1, 2, 3}
# B = {1, 2, 3, 4, 5}
# print(A.issubset(B))  # Output: True
# print(A <= B)  # Sama dengan issubset

# issuperset() - mengecek apakah superset
# print(B.issuperset(A))  # Output: True
# print(B >= A)  # Sama dengan issuperset

# isdisjoint() - mengecek apakah tidak ada elemen yang sama
# C = {6, 7, 8}
# print(A.isdisjoint(C))  # Output: True


# E. Frozen Set (SET YANG TIDAK BISA DIUBAH)

# Membuat frozenset
# fs = frozenset([1, 2, 3, 4, 5])

# Tidak bisa diubah
# fs.add(6)  # Error! AttributeError

# Bisa digunakan sebagai key dictionary atau elemen set lain
# dict_dengan_frozenset = {fs: "nilai"}
# set_of_sets = {frozenset([1, 2]), frozenset([3, 4])}

# Operasi matematika tetap bisa dilakukan
# fs2 = frozenset([4, 5, 6])
# print(fs | fs2)  # Union works
# print(fs & fs2)  # Intersection works


"""
F. Kapan Menggunakan Set?
Gunakan Set ketika:
    1. Perlu menyimpan nilai unik (tidak ada duplikat)
    2. Perlu operasi matematika himpunan (union, intersection, dll)
    3. Perlu pengecekan membership yang cepat (O(1))
    4. Urutan data tidak penting
    5. Perlu menghilangkan duplikat dari koleksi
Jangan gunakan Set ketika:

    1. Perlu akses berdasarkan index
    2. Perlu menjaga urutan elemen
    3. Perlu menyimpan elemen duplikat
    4. Perlu menyimpan elemen mutable (list, dict, set)
"""