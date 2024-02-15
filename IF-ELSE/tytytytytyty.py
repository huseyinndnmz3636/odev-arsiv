import random

def tahta():
    print("taş,kağıt,makas,kertenkele,spock oyununa Hoş geldiniz!")
    print("Seçenekler:0 - taş,1 - kağıt,2 - makas,3 - kertenkele,4 - spock")
    
def kullanici_secimi():
    secim = int(input("Lütfen seçiminizi yapınız (0-4): "))
    while secim not in range(5):
        print("Geçersiz seçim. Lütfen 0 ile 4 arasında bir sayı girin. ")