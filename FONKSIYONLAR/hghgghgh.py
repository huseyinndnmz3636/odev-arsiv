def selamla(isim):
    return "Merhaba , " + isim + "Dönmez"
 
def fonksiyon_cagir(f, parametre):
    return f(parametre)


isim = "Hüseyin "
selam_mesaji = fonksiyon_cagir(selamla, isim)
print(selam_mesaji)



