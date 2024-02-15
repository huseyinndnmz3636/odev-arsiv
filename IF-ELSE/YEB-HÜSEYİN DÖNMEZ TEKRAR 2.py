def kelimeyi_yazdir(kelime, sayi):
    for i in range(sayi):
        print(kelime)
kelime = input("Bir kelime girin: ")
sayi = int(input("Kelimeyi kaç kez yazdırmak istersiniz? "))
 
kelimeyi_yazdir(kelime, sayi)