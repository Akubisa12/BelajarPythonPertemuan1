#index :urutan elemen
# index = n-1
# index selalu dimulai dari 0
list_1 = [2, 4, 8, 16]
#  2 indeks ke 0
#  4 indeks ke 1
#  8 indeks ke 2
# 16 indeks ke 3 
# print(list_1)
# lebih dari satu tipe data :
# 24 : int
# False : boolean
# "Hello Python" : string
list_3 = [24, False, "Hello Python"]
# print(list_3[0])
list_3.append(2)
list_3.remove(False)

# print(list_3)
# print(list_3)
# print(list_3)

a = [2, 5, 6, 7]

# Use append() to add the element 8 to the end of the list
a.append(8)
# print(a)


fruits = ["apple", "banana", "cherry"]
new_fruits = fruits.copy()
# print(new_fruits) # Output: ['apple', 'banana', 'cherry']

# slicing
fruits = ["apple", "banana", "cherry"]
new_fruits = fruits[:-3]
print("before slice")
print(fruits) # Output: ['apple', 'banana', 'cherry']
print("after slice")
print(new_fruits)