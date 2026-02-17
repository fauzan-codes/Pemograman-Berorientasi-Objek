number = [0] * 10
ganjil = 0
genap = 0

for i in range(10):
    number[i] = int(input(f"Masukkan angka ke-{i+1} : "))

    if number[i] % 2 == 0:
        genap = genap + 1
    else:
        ganjil =+ ganjil + 1

print()
print(f"Total : {sum(number)}")
print(f"Rata Rata : {sum(number)/len(number)}")
print(f"angka Terbesar : {max(number)}")
print(f"angka Terkecil : {min(number)}")
print(f"Jumlah Angka Ganjil : {ganjil}")
print(f"Jumlah Angka Genap : {genap}")
