import os
import datetime
import time

def bilgisayari_kapat(saat, dakika):
    su_an = datetime.datetime.now()
    kapanma_zamani = su_an.replace(hour=saat, minute=dakika, second=0, microsecond=0)

    if su_an > kapanma_zamani:
        kapanma_zamani += datetime.timedelta(days=1)  # Eğer girilen zaman bugünden önceyse, bir gün ekleyerek yarına atar

    kalan_zaman = kapanma_zamani - su_an
    kalan_saniye = kalan_zaman.total_seconds()

    print(f"Bilgisayar kapanacak saat: {saat}:{dakika}")
    print(f"Kalan zaman: {int(kalan_saniye // 3600)} saat {int((kalan_saniye % 3600) // 60)} dakika")

    time.sleep(kalan_saniye)
    os.system("shutdown /s /t 1")  # Windows için
    # os.system("shutdown now")  # Linux için

def main():
    try:
        saat = int(input("Kapatılacak saat (0-23): "))
        dakika = int(input("Kapatılacak dakika (0-59): "))

        if 0 <= saat <= 23 and 0 <= dakika <= 59:
            bilgisayari_kapat(saat, dakika)
        else:
            print("Geçersiz saat veya dakika girdiniz.")
    except ValueError:
        print("Lütfen geçerli bir sayı girin.")

if __name__ == "__main__":
    main()
    