kalimat = input("Masukan sebuah kalimat yang anda inginkan: ")

list_karakter = list(kalimat)

set_karakter_unik = set(kalimat)

tuple_karakter_unik = tuple(set_karakter_unik)

dict_frekuensi = {}

for char in kalimat:
    if char in dict_frekuensi:
        dict_frekuensi[char] += 1
    else:
        dict_frekuensi[char] = 1

print("\n=== Hasil ===")
print(f"Jumlah total karakter: {len(list_karakter)}")
print(f"Jumlah karakter unik: {len(set_karakter_unik)}")
print(f"Karakter unik (set): {set_karakter_unik}")
print(f"Karakter unik (tuple): {tuple_karakter_unik}")
print(f"Frekuensi karakter: {dict_frekuensi}")