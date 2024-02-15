from datetime import datetime
 
# Kullanıcının doğum tarihini al
yil = int(input("Doğum yılınızı girin: "))
ay = int(input("Doğum ayınızı girin: "))
gun = int(input("Doğum gününüzü girin: "))
 
# Bugünün tarihini al
bugun = datetime.now()
 
# Yaşı hesapla
yas = bugun.year - yil
 
print("Yaşınız:\n", yas)