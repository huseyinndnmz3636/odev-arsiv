import random

def tahta():
    print("Taş, Kağıt, Makas, Kertenkele, Spock oyununa hoş geldiniz!")
    print("Seçenekler: 0 - Taş, 1 - Kağıt, 2 - Makas, 3 - Kertenkele, 4 - Spock")

def kullanici_secimi():
    secim = int(input("Lütfen seçiminizi yapın (0-4): "))
    while secim not in range(5):
        print("Geçersiz seçim. Lütfen 0 ile 4 arasında bir sayı girin.")
        secim = int(input("Lütfen seçiminizi yapın (0-4): "))
    return secim

def bilgisayar_secimi():
    return random.randint(0, 4)

def sonucu_belirle(kullanici, bilgisayar):
    if kullanici == bilgisayar:
        return "Berabere!"
    elif (kullanici - bilgisayar) % 5 in [1, 3]:
        return "Kazandınız!"
    else:
        return "Kaybettiniz."

def main():
    tahta()
    kullanici = kullanici_secimi()
    bilgisayar = bilgisayar_secimi()

    print(f"Siz: {kullanici}")
    print(f"Bilgisayar: {bilgisayar}")

    sonuc = sonucu_belirle(kullanici, bilgisayar)
    print(sonuc)

if __name__ == "__main__":
    main()
