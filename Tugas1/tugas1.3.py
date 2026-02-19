namaD = input("Masukkan nama depan anda : ")
namaB = input("Masukkan nama belakang anda : ")

namaLengkap = f"{namaD} {namaB}"
listNama = list(namaLengkap)
listNama.reverse()

namaTerbalik = ''.join(listNama)
  
print("")
print(f"Nama lengkap  : {namaLengkap}")
print(f"Nama Terbalik : {namaTerbalik}")