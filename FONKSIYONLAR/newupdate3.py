# Bu bir örnek Python kodudur

def karsilama_mesaji():
    ad = input("Adınızı girin: ")
    print("Merhaba, " + ad + "! Hoş geldiniz.")

def toplama(a, b):
    return a + b

def cikarma(a, b):
    return a - b

def carpma(a, b):
    return a * b

def bolme(a, b):
    if b != 0:
        return a / b
    else:
        return "Bir sayıyı sıfıra bölemezsiniz."

if __name__ == "__main__":
    karsilama_mesaji()

    sayi1 = float(input("Birinci sayıyı girin: "))
    sayi2 = float(input("İkinci sayıyı girin: "))

    toplam = toplama(sayi1, sayi2)
    fark = cikarma(sayi1, sayi2)
    carpim = carpma(sayi1, sayi2)
    bolum = bolme(sayi1, sayi2)

    print("Toplam:", toplam)
    print("Fark:", fark)
    print("Çarpım:", carpim)
    print("Bölüm:", bolum)
