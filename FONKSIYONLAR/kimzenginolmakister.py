import random

class KimMilyonerOlmakIster:
    def __init__(self, soru_dosyasi):
        self.sorular = self.sorulari_yukle(soru_dosyasi)
        self.suan_ki_soru = None
        self.soru_index = 0
        self.para_odulleri = [500, 1000, 2000, 3000, 5000, 7500, 15000, 30000, 60000, 125000, 250000, 500000, 1000000]

    def sorulari_yukle(self, dosya_adi):
        with open(dosya_adi, 'r', encoding='utf-8') as dosya:
            satirlar = dosya.readlines()

        sorular = []
        for i in range(0, len(satirlar), 6):
            soru_metni = satirlar[i].strip()
            secenekler = [satirlar[i + j].strip() for j in range(1, 5)]
            dogru_cevap = satirlar[i + 5].strip()
            sorular.append({'soru': soru_metni, 'secenekler': secenekler, 'dogru_cevap': dogru_cevap})

        return sorular

    def soru_goster(self):
        soru = self.sorular[self.soru_index]
        self.suan_ki_soru = soru
        print(f"Soru {self.soru_index + 1}: {soru['soru']}")
        for i, secenek in enumerate(soru['secenekler'], start=1):
            print(f"{i}. {secenek}")
    
    def cevap_kontrol(self, cevap):
        dogru_cevap = self.suan_ki_soru['dogru_cevap']
        return cevap.lower() == dogru_cevap.lower()

    def oyunu_baslat(self):
        print("Kim Milyoner Olmak İster oyununa hoş geldiniz!\n")
        while self.soru_index < len(self.sorular):
            self.soru_goster()
            cevap = input("Cevabınızı girin (çıkış için 'q'): ")
            if cevap.lower() == 'q':
                print("\nOyunu iptal ettiniz. Toplam kazandığınız para: 0 TL")
                break
            elif self.cevap_kontrol(cevap):
                print("Doğru cevap!\n")
                self.soru_index += 1
                if self.soru_index < len(self.sorular):
                    print(f"Şu ana kadar kazandığınız para: {self.para_odulleri[self.soru_index - 1]} TL\n")
            else:
                print("Yanlış cevap! Oyunu kaybettiniz.")
                print(f"Toplam kazandığınız para: {self.para_odulleri[max(0, self.soru_index - 1)]} TL")
                break

        if self.soru_index == len(self.sorular):
            print("Tebrikler! Oyunu başarıyla tamamladınız. Toplam kazandığınız para: 1.000.000 TL")

if __name__ == "__main__":
    soru_dosyasi = "kim_milyoner_olmak_ister_sorular.txt"
    oyun = KimMilyonerOlmakIster(soru_dosyasi)
    oyun.oyunu_baslat()
