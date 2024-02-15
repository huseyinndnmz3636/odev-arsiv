#Bu program, kullanıcı her Enter tuşuna bastığında bir zar atar ve atılan zarın değerini ekrana yazdırır. Kullanıcı başka bir zar atmak isterse 'e' veya 'E' tuşuna basabilir, aksi takdirde program sona erer. Bu sadece basit bir simülasyon örneğidir ve isteğinize göre daha fazla özellik ekleyebilirsiniz.

import random

def zar_at():
    return random.randint(1, 6)

if __name__ == "__main__":
    while True:
        input("Zar atmak için Enter tuşuna basın...")
        
        zar_degeri = zar_at()
        print(f"Atılan zar: {zar_degeri}")

        devam_et = input("Başka bir zar atmak ister misiniz? (Evet için 'e' veya 'E', Hayır için başka bir tuş): ")
        if devam_et.lower() != 'e':
            print("Oyun sona erdi. İyi günler!")
            break
        