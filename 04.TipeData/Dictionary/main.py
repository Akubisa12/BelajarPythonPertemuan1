"""
Pengertian DictionaryDictionary adalah struktur data di Python yang menyimpan data dalam bentuk pasangan key-value (kunci-nilai). Dictionary bersifat:
    Mutable (dapat diubah)
    Unordered (tidak berurutan, meski Python 3.7+ menjaga urutan insersi)
    Indexed menggunakan key, bukan index numerik
    Key harus unik dan immutable (string, number, tuple)
"""

# Membuat Dictionary
# Dictionary kosong
dict_kosong = {}
dict_kosong2 = dict()

# Dictionary dengan data
mahasiswa = {
    "nama": "Budi",
    "nim": "12345",
    "jurusan": "Informatika",
    "ipk": 3.75
}

# Dictionary dengan berbagai tipe data
data_mixed = {
    "angka": 100,
    "list": [1, 2, 3],
    "tuple": (4, 5, 6),
    "dict": {"nested": "value"}
}


# mengakses elemen menggunakan key dan method get di dictionary
# mahasiswa = {"nama": "Budi", "nim": "12345", "ipk": 3.75}

# Menggunakan key
# print(mahasiswa["nama"])  # Output: Budi

# Menggunakan method get() - lebih aman
# print(mahasiswa.get("nim"))  # Output: 12345
# print(mahasiswa.get("alamat"))  # Output: None (tidak error)
# print(mahasiswa.get("alamat", "Tidak ada"))  # Output: Tidak ada

# Menambah dan mengubah data di dalam dictionary
# mahasiswa = {"nama": "Budi", "nim": "12345"}

# Menambah data baru
# mahasiswa["jurusan"] = "Informatika"

# Mengubah data yang ada
# mahasiswa["nama"] = "Budi Santoso"

# Update multiple items sekaligus
# mahasiswa.update({"ipk": 3.8, "semester": 5})

# print(mahasiswa)

# Menghapus data didalam dictionary
# mahasiswa = {"nama": "Budi", "nim": "12345", "ipk": 3.75}

# Menghapus dengan key tertentu
# del mahasiswa["ipk"]

# Menghapus dan mengembalikan value
# nim = mahasiswa.pop("nim")
# print(nim)  # Output: 12345

# Menghapus item terakhir (Python 3.7+)
# item = mahasiswa.popitem()

# Menghapus semua item
# mahasiswa.clear()

# Method penting dan sering digunakan didalam dictionary
# mahasiswa = {"nama": "Budi", "nim": "12345", "ipk": 3.75}

# keys() - mendapatkan semua key
# print(mahasiswa.keys())  # dict_keys(['nama', 'nim', 'ipk'])

# values() - mendapatkan semua value
# print(mahasiswa.values())  # dict_values(['Budi', '12345', 3.75])

# items() - mendapatkan pasangan key-value
# print(mahasiswa.items())  # dict_items([('nama', 'Budi'), ...])

# len() - jumlah item
# print(len(mahasiswa))  # Output: 3

# in - mengecek keberadaan key
# print("nama" in mahasiswa)  # Output: True

# Menyalin dictionary
# original = {"a": 1, "b": 2}

# Shallow copy (referensi berbeda)
# copy1 = original.copy()
# copy2 = dict(original)

# Deep copy (untuk nested dict)
# import copy
# nested = {"a": {"b": 1}}
# deep = copy.deepcopy(nested)