with open("harcama_listesi.txt", "w", encoding="utf-8") as f:
    pass  # dosya içini temizleme


def harcama_ekle():
    kategori = input("Kategori: ")
    tutar = int(input("Tutar: "))
    aciklama = input("Açıklama: ")

    with open("harcama_listesi.txt", "a", encoding="utf-8") as myFile:
        myFile.write(f"{kategori},{tutar}, {aciklama}\n")

    return "Harcama eklendi"


def harcamalari_listele():
    with open("harcama_listesi.txt", "r", encoding="utf-8") as myFile:
        return myFile.read().splitlines()

def harcamalari_hesapla():
    total = 0


    with open("harcama_listesi.txt", "r", encoding="utf-8") as myFile:
        for satir in myFile:
            kategori, tutar, aciklama = satir.strip().split(",") #kategori = (satir.strip().split(","))[0] de diyebilirdik
            tutar = int(tutar)
            total = total + tutar
    return total

def kategoriye_gore_harcama(kategori_adi):

    with open("harcama_listesi.txt", "r", encoding="utf-8") as myFile:
        total = 0
        for satir in myFile:
            kategori, tutar, aciklama = satir.strip().split(",") #aynı isimli oldukları için burada bir ezme oldu
            if kategori.lower() == kategori_adi.lower():
                total = total + int(tutar)

    return total



while True:

    print("\n1- Harcama Ekle\n2- Harcamaları Listele\n3- Toplam Harcama\n"
          "4- Kategoriye göre harcama\n5- Çıkış")

    choice = input("Choice: ")

    if choice == "1":
        mesaj = harcama_ekle()
        print(mesaj)
    elif choice == "2":
        mesaj = harcamalari_listele()

        for satir in mesaj:
            kategori,tutar,aciklama = satir.split(",")
            print(f"Kategori: {kategori} | Tutar: {tutar} | Açıklama: {aciklama}")
    elif choice == "3":
        tutar = harcamalari_hesapla()
        print(f"Toplam harcama {tutar}")
    elif choice == "4":
        kategori = input("Kategori adı: ")
        toplam = kategoriye_gore_harcama(kategori)
        print(f"Kategori: {kategori}, toplam harcama: {toplam}")
    elif choice == "5":
        print("Goodbye")
        break
