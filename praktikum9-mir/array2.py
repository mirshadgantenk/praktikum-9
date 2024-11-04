# deklarasi matrix pertama dan kedua 
matriks1 = []
matriks2 = []

# meminta input untuk matrix pertma 
print("masukan elemen untuk matriks pertama (3x3):")
for i in range(3):
    baris = []
    for j in range(3):
        nilai = int(input(f"masukan elemen baris {i+1}, kolom {j+1}: "))
        baris.append(nilai)
    matriks1.append(baris)

#meminta input untuk matrix kedua 
print("\nmasukan elemen untuk matriks kedua (3x3):")
for i in range(3):
    baris = []
    for j in range(3):
        nilai = int(input(f"masukan elemen baris {i+1}, kolom {j+1}: "))
        baris.append(nilai)
    matriks2.append(baris)

# meminta input jenis oprasi
operasi = input("\npilih operasi (penjumlahan/penguranagan/perkalian): ").lower()

# melakukan operasi berdasarkan pilihan
hasil = []
if operasi == ' penjumlahan':
    for i in range(3):
        baris = []
        for j in range(3):
            baris.append(matriks1[i][j] - matriks2[i][j])
            hasil.append(baris)
elif operasi == 'pengurangan':
    for i in range(3):
        baris =[]
        for j in range(3):
            baris.append(baris)
        hasil.append(baris)
elif operasi == 'perkalian':
    for i in range(3):
        baris = []
        for j in range(3):
            nilai = 0
            for k in range(3):
                nilai += matriks1[i][k] * matriks2[k][j]
            baris.append(nilai)
            hasil.append(baris)
else:
    print(f"operasi tidak valid")

#menampilkan hasil operasi
if hasil:
    print(f"\nhasil {operasi} matriks:")
for baris in hasil:
        print(baris)