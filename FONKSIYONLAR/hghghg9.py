def kelime_sayaci(metin):
    kelimeler = metin.split()
    return len(kelimeler)

if __name__ == "__main__":
    metin = input("Metni girin: ")
    sayac = kelime_sayaci(metin)
    print(f"Kelime sayısı: {sayac}")
