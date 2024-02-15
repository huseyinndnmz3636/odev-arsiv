import random
import string

def yeni_sifre_olustur(uzunluk=8):
    # Şifrede kullanılacak karakterler
    karakterler = string.ascii_letters + string.digits + string.punctuation

    # Şifreyi oluştur
    yeni_sifre = ''.join(random.choice(karakterler) for i in range(uzunluk))

    return yeni_sifre

if __name__ == "__main__":
    uzunluk = int(input("Yeni şifrenin uzunluğunu belirtin: "))

    if uzunluk <= 0:
        print("Uzunluk 0'dan büyük olmalıdır.")
    else:
        sifre = yeni_sifre_olustur(uzunluk)
        print("Yeni şifre:", sifre)
