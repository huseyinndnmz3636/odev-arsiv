def basamak_kupleri_toplami(sayi):
    yuzler_basamagi = sayi // 100
    onlar_basamagi = (sayi % 100) // 10
    birler_basamagi = sayi % 10
    
    kupler_toplami = yuzler_basamagi ** 3 + onlar_basamagi ** 3 + birler_basamagi ** 3
    
    return kupler_toplami

def main():
    sayi = int(input("Üç basamaklı bir sayı girin: "))
    
    if sayi < 100 or sayi > 999:
        print("Geçersiz giriş. Lütfen üç basamaklı bir sayı girin.")
    else:
        toplam = basamak_kupleri_toplami(sayi)
        if toplam == sayi:
            print(f"{sayi} sayısı Armstrong sayıdır.")
       
