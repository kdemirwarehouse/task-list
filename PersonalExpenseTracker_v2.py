#csv formatına geçiş + try/ except
import csv

with open("harcama_listesi.csv", "w", newline ="",encoding="utf-8") as file:
    writer = csv.writer(file)  # dosya içini temizleme
    writer.writerow(["kategori", "tutar", "aciklama"])


def harcama_ekle():
    kategori = input("Kategori: ")
    try:
        tutar = int(input("Tutar: "))
    except ValueError:
        print("Değer sayı olmalı")
        return

    aciklama = input("Açıklama: ")

    with open("harcama_listesi.csv", "a", newline = "", encoding="utf-8") as myFile:
        writer = csv.writer(myFile)
        writer.writerow([kategori,tutar,aciklama])

    return "Harcama eklendi"


def harcamalari_listele():

    try:
        with open("harcama_listesi.csv", "r", encoding="utf-8") as myFile:
                reader = csv.DictReader(myFile)
                bos_mu = True
                for row in reader:
                    print (row)
                    bos_mu = False

                if bos_mu:
                    print("Henüz harcama yok")

    except FileNotFoundError:
        print("Harcama dosyası bulunamadı")


def harcamalari_hesapla():
    total = 0


    with open("harcama_listesi.csv", "r", encoding="utf-8") as myFile:
        reader = csv.DictReader(myFile)
        for row in reader:
            try:
                total += int(row["tutar"])
            except (ValueError, KeyError):
                continue
    return total


def kategoriye_gore_harcama(kategori_adi):
    total = 0

    with open("harcama_listesi.csv", "r", encoding="utf-8") as myFile:
        reader = csv.DictReader(myFile)
        for row in reader:
            try:
                if row["kategori"].lower() == kategori_adi.lower():
                        total = total + int(row["tutar"])
            except (ValueError, KeyError):
                continue

    return total


while True:

    print("\n1- Harcama Ekle\n2- Harcamaları Listele\n3- Toplam Harcama\n"
          "4- Kategoriye göre harcama\n5- Çıkış")

    choice = input("Choice: ")

    if choice == "1":
        mesaj = harcama_ekle()
        print(mesaj)

    elif choice == "2":
        harcamalari_listele()

    elif choice == "3":
        tutar = harcamalari_hesapla()
        print(f"Toplam harcama: {tutar}")
    elif choice == "4":
        kategori = input("Kategori adı: ")
        toplam = kategoriye_gore_harcama(kategori)
        print(f"Kategori: {kategori}, toplam harcama: {toplam}")
    elif choice == "5":
        print("Goodbye")
        break

