def ders_saati_toplam(dersler):
    toplam_saat = sum(dersler)
    toplam_ders = len(dersler)
    return toplam_saat, toplam_ders

dersler = []

ders_sayisi = int(input("Kaç dini ders olduğunu girin: "))

for i in range(ders_sayisi):
    ders_saati = int(input(f"{i + 1}. dini dersin saatini girin: "))
    dersler.append(ders_saati)

toplam_saat, toplam_ders = ders_saati_toplam(dersler)

print(f"Toplam dini ders saati: {toplam_saat} saat")
print(f"Toplam dini ders sayısı: {toplam_ders}")
