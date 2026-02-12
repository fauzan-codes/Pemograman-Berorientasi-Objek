number = [0] * 10
total = 0
terbesar = 0
terkecil = 9999999
ganjil = 0
genap = 0


for i in range(10):
    number[i] = int(input(f"Masukkan angka ke-{i+1} : "))

    total = total + number[i]
    if terbesar < number[i]:
        terbesar = number[i]
    if terkecil > number[i]:
        terkecil = number[i]

    if number[i] % 2 == 0:
        genap = genap + 1
    else:
        ganjil =+ ganjil + 1

print()
print(f"Total : {total}")
print(f"Rata Rata : {total/len(number)}")
print(f"angka Terbesar : {terbesar}")
print(f"angka Terkecil : {terkecil}")
print(f"Jumlah Angka Ganjil : {ganjil}")
print(f"Jumlah Angka Genap : {genap}")
