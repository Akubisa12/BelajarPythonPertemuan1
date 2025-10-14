message1 = "hello world"
message2 = message1
message3 = "hello Jessen"
# alamat memori itu bersifat unik antar variabel. 
# karena UNIK sudah pasti alamat memori dari setiap variabel akan berbeda beda TIDAK AKAN SAMA
# mengapa alamat message1 bisa sama dengan alamat message2 ? karena di baris kedua kita nyatakan bahwasannya message2 = message1
print(f": message 1, id: {message1}, data: {id(message1)}")
print(f": message 1, id: {message2}, data: {id(message2)}")
print(f": message 1, id: {message3}, data: {id(message3)}")