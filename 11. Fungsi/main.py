# Secara sederhana, fungsi adalah sekumpulan instruksi yang diberi nama untuk melakukan tugas tertentu. Sama seperti kamu punya resep untuk membuat kopi
# Anggaplah kita ingin menulis resep(membuat fungsi) untuk membuat berbagai jenis kopi

# 1. Mendefinisikan fungsi (Resep kopi)
# Pertama, kita tulis resepnya, Dalam python ini disebut "mendefinisikan fungsi" menggunakan def (define). Selain itu, resep ini juga butuh beberapa bahan(parameter)

# CONTOH SEDERHANA FUNGSI 
def buat_kopi(jenis_kopi, pakai_gula, pakai_susu):
    print(f"Mulai membuat {jenis_kopi}....")

    kopi = f"Secangkir {jenis_kopi}"

    if pakai_gula:
        print("Menambahkan gula...")
        kopi += " dengan gula"
    
    if pakai_susu:
        print("Menambahkan susu...")
        kopi += " dan susu"
    
    print("Kopi selesai dibuat!")
    return kopi # ini adalah hasil akhir kopi nya

# Sekarang resepnya sudah jadi, kita bisa mulai membuat kopi kapan pun kita mau. 
# Proses menggunakan resep ini disebut calling function (memanggil fungsi)
# Saat memanggil fungsi, kita menyediakan bahan-bahan yang sebenarnya. 
# Bahan-bahan ini disebut argumen 

# Contoh 1 : Membuat kopi hitam pahit 
# Kita mau kopi hitam, tanpa gula, dan tanpa susu

kopi_pagiku = buat_kopi("Kopi Hitam", pakai_gula=False, pakai_susu=False)
print("\n----Pesanan 1------")
print(f"Hasilnya: {kopi_pagiku}")

# Contoh 2 : Membuat kopi susu manis 
# Sekarang teman kamu mau kopi tubruk, pkai gula dan pakai susu
kopi_teman = buat_kopi("Kopi Tubruk", pakai_gula=True, pakai_susu=True)
print("\n----Pesanan 2------")
print(f"Hasilnya: {kopi_teman}")


# Q : Lalu apa bedanya menggunakan return dengan tdk menggunakan return ?
# A : Oke, kita analogikan sebagai barista kopi kita. Sederhana nya Fungsi tanpa return seperti seorang barista yang mengumumkan kalau kopi km sudah jadi. Sedangkan fungsi dengan return value seperti barista yang sedang menyerahkan secangkir kopi langsung ke tangan kamu.
# Oke kita bedah 1 per satu 
# 1. Fungsi tanpa return
# Fungsi melakukan sebuah aksi atau pekerjaan, tapi tidak memberikan nilai apa pun kembali ke program. Tugasnya selesai begitu saja di dalam fungsi itu. Dalam Python, fungsi yang tidak memiliki return secara eksplisit/langsung akan otomatis mengembalikan nilai spesial yaitu NONE
# Contoh analogi nya : Barista yang hanya berteriak, "Kopi untuk B sudah siap di meja nomor 5!"
# Lalu Aksinya adalah : Dia membuat kopi dan memberitahu si B
# Nah hasil nya untuk si B : Si B mendapat informasi, tapi si B belum memegang kopinya. Program si B tidak mendapatkan "benda" apa pun untuk "diolah lebih lanjut"


# CONTOH DALAM PROGRAM 
def umumkan_kopi_siap(jenis_kopi):
    print(f"Pemberitahuan: {jenis_kopi} Anda sudah siap!")
umumkan_kopi_siap("Espresso")

status_pesanan = umumkan_kopi_siap("Late")
print(f"Isi variabel status_pesanan adalah: {status_pesanan}") # NONE

# 2. Fungsi dengan return 
# Fungsi ini melakukan sebuah pekerjaan DAN memberikan hasil kembali ke baris kode yang memanggilnya. Hasil ini bisa disimpan dalam variabel, digunakan untuk perhitungan lain, atau diberikan ke fungsi lain.
# Contoh analogi nya : Barista membuat kopi lalu menyerahkan langsung kopi itu ke si B 
# Lalu aksi nya adalah : Dia membuat kopi untuk si B
# Dan hasil nya untuk si B : si B mendapatkan secangkir kopi(sebuah objek/nilai) yang bisa si B minum, berikan ke teman, atau foto

# CONTOH DALAM KODE
def buat_kopi(jenis_kopi):
    print(f"Meracik {jenis_kopi}....")
    return f"Secangkir {jenis_kopi} panas"

kopi_saya = buat_kopi("Cappuccino")

print(f"Yang saya pegang sekarang: {kopi_saya}")
print(f"Saya akan menerima {kopi_saya.replace('panas', 'nikmat')} ini.")

# Contoh salah kaprah vs Praktik terbaik 
# Bayangkan kita ingin membuat fungsi untuk mejumlahkan dua angka dan hasilnya ingin kita kalikan dua 
# contoh yang salah (menggunakan print)
# Bayangkan kita ingin membuat fungsi untuk menjumlahkan dua angka dan hasilnya ingin kita kalikan dua
def jumlahkan_dan_cetak(a,b):
    hasil = a + b 
    print(f"Hasil penjumlahan adalah {hasil}") # 15
jumlahkan_dan_cetak(10,5)
# hasil_akhir = penjumlahan * 2 -> ERROR
print(f"Isi variabel penjumlahan {penjumlahan}") # NONE

# Kode diata gagal karena penjumlahan berisi None, dan None tidak bisa dikalikan dua. Fungsi ini tidak berguna untuk program kita, hanya berguna untuk memberi tahu pengguna

# contoh yang benar (menggunakan return)
def jumlahkan_dan_kembalikan(a,b):
    hasil = a + b
penjumlahan = jumlahkan_dan_kembalikan(10,5)
hasil_akhir = penjumlahan * 2 
print(f"Nilai yang dikembalikan fungsi: {penjumlahan}")
print(f"Hasil akhirnya setelah dikali dua: {hasil_akhir}")