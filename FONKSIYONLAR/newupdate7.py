def ortalama_hesaplama(liste):
    toplam = sum(liste)
    adet = len(liste)
    ortalama = toplam / adet
    print(f"Girilen sayıların ortalaması{ortalama}")
    

ortalama_hesaplama([1,2,3,4,5,6,7])