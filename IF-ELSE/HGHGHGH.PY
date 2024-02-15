import os
import time

def bilgisayari_kapat(saat, dakika):
    while True:
        su_an = time.localtime()
        if su_an.tm_hour == saat and su_an.tm_min == dakika:
            print(f"Bilgisayar kapanacak saat: {saat}:{dakika}")
            os.system("shutdown /s /t 1")  # Windows için
            # os.system("shutdown now")  # Linux için
            break
        else:
            print(f"Saat: {su_an.tm_hour}:{su_an.tm_min} - Bekleniyor...")
            time.sleep(60)  # Her dakika kontrol et

# Bilgisayarı saat 20:30'da kapatmak için
bilgisayari_kapat(11, 45)
