def selamla(isim):
    return "Hey tatlı şey " + isim + "varsın;)"
 
def fonksiyon_cagir(f, parametre):
    return f(parametre)


isim = "iyiki"
selam_mesaji = fonksiyon_cagir(selamla, isim)
print(selam_mesaji)