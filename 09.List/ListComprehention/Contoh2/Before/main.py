seq = []

#PENJABARAN PERULANGAN
# i = 0
# 0 dibagi 2 sisany adalah 0 lalu kita cek apakah 0 == 1 ? FALSE
# isi seq saat ini : []

# i = 1 
# 1 dibagi 2 sisanya adalah 1, lalu kita cek apakah 1 == 1 ? TRUE
# isi seq saat ini : [1]

# i = 2 
# 2 dibagi 2 sisanya adalah 0, lalu kita cek apakah 0 == 1 ? FALSE
# isi seq saat ini : [1]

# i = 3 
# 3 dibagi 2 sisanya adalah 1, lalu kita cek apakah 1 == 1 ? TRUE
# isi seq saat ini : [1,3]

# i = 4 
# 4 dibagi 2 sisanya 0, lalu kita cek apakah 0 == 1 ? FALSE
# isi seq saat ini : [1,3]

# i = 5 
# 5 dibagi 2 sisanya 1, lalu kita cek apakah 1 == 1 ? TRUE 
# isi seq saat ini : [1,3,5]

# i = 6
# 6 dibagi 2 sisanya 0, lalu kita cek apakah 0 == 1 ? FALSE 
# isi seq saat ini : [1,3,5]

# i = 7 
# 7 dibagi 2 sisanya 1, lalu kita cek apakah 1 == 1 ? TRUE
# # isi seq saat ini : [1,3,5,7]

# i = 8
# 8 dibagi 2 sisanya 0, lalu kita cek apakah 0 == 1 ? FALSE
# isi seq saat ini : [1,3,5,7]

# i = 9
# 9 dibagi 2 sisanya 1, lalu kita cek apakah 1 == 1 ? TRUE
#isi seq saat ini : [1,3,5,7,9]
for i in range(10):
    if i % 2 == 1 :
        seq.append(i)
print(seq) #isi seq saat ini : [1,3,5,7,9]