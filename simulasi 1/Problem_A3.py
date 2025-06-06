suara = [0, 0, 0, 0, 0, 0, 0]
total = 0
naik = 0
turun = 0
konstan = 0

for i in range(7):
    suara[i] = int(input(f"Masukkan suara pada hari ke-{i + 1}:"))
    if suara[i] >= 80:
        waktu = int(input("Berapa lama suara(jam):"))
        if waktu >= 8:
            menjauh = (suara[i] - 80)
            total += suara[i]
            print(
                f"Peringatan suara besar dan kontinu, segera menjauh {menjauh} m dari sumber suara pada hari ke-{i + 1}")
            print("")
        else:
            total += suara[i]
            print(f"Peringatan suara besar dan diskontinu pada hari ke-{i + 1}")
            print("_")
    elif suara[i] >= 1 and suara[i] < 80:
        waktu = int(input("Berapa lama suara(jam):"))
        if waktu >= 4:
            total += suara[i]
            print(f"Peringatan suara kecil dan kontinu pada hari ke-{i + 1}")
            print("")
        else:
            print(f"Tidak ada peringatan pada hari ke-{i + 1}")
            print("")
    else:
        print("Tidak terdapat suara")
        print("")

for i in range(7):
    if suara[i] > suara[i + 1]:
        turun += 1
        print(f"Desibel suara menurun pada hari ke-{i + 2}")
    elif suara[i] < suara[i + 1]:
        naik += 1
        print(f"Desibel suara naik pada hari ke-{i + 2}")
    else:
        konstan += 1
        print(f"Desibel suara konstan pada hari ke-{i + 2}")
    if i == 5:
        break

if naik > turun:
    print("Desibel relatif meningkat dalam seminggu")

elif naik < turun:
    print("Desibel suara relatif menurun dalam seminggu")

else:
    print("Desibel suara relatif konstan dalam seminggu")

makshimum = suara[0]
minumum = suara[0]

for i in range(1, 7):
    if suara[i] > makshimum:
        makshimum = suara[i]
    if suara[i] < minumum:
        minumum = suara[i]

print(f"Nilai suara maksimum:{makshimum} db")
print(f"nilai suara minimum adalah {minumum} db")
rata = total / 7
print(f"Rata-rata suara dalam interval satu minggu adalah {rata} db")