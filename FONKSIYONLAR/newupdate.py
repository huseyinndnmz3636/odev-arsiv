def asal_mi(sayi):
    if sayi < 2:
        return False
    for i in range(2, int(sayi ** 0.5) + 1):
        if sayi % i == 0:
            return False
    return True

def asal_sayilari_bul(sinir):
    asal_sayilar = []
    for sayi in range(2, sinir):
        if asal_mi(sayi):
            asal_sayilar.append(sayi)
    return asal_sayilar

sinir = int(input("Asal sayıları bulmak için bir üst sınır girin: "))
asal_listesi = asal_sayilari_bul(sinir)
print(f"{sinir} sayısına kadar olan asal sayılar: {asal_listesi}")
