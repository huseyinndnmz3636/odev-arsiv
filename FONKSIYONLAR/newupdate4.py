import math

def toplama(sayi1, sayi2):
    return sayi1 + sayi2

def cikarma(sayi1, sayi2):
    return sayi1 - sayi2

def bolme(sayi1, sayi2):
    if sayi2 != 0:
        return sayi1 / sayi2
    else:
        return "Bir sayıyı sıfıra bölemezsiniz."

def carpma(sayi1, sayi2):
    return sayi1 * sayi2

def karekok_alma(sayi):
    if sayi >= 0:
        return math.sqrt(sayi)
    else:
        return "Negatif bir sayının karekökü alınamaz."

if __name__ == "__main__":
    sayi1 = float(input("Birinci sayıyı girin: "))
    sayi2 = float(input("İkinci sayıyı girin: "))

    print("Toplam:", toplama(sayi1, sayi2))
    print("Fark:", cikarma(sayi1, sayi2))
    print("Çarpım:", carpma(sayi1, sayi2))
    print("Bölüm:", bolme(sayi1, sayi2))
    
    # Kare kök alma işlemi için sadece bir sayı gereklidir
    sayi3 = float(input("Karekök alınacak sayıyı girin: "))
    print("Karekök:", karekok_alma(sayi3))
