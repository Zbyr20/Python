#1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
# a = int(input('bir sayı giriniz: '))
# rs = (a < 100) and (a > 0)
# print(rs)

#Girilen bir sayının pozitif çift sayı olup olmadığnı kontrol ediniz.

# a = int(input('bir sayı giriniz:'))
# rs = (a > 0) and (a % 2 == 0)
# print(rs)

#Email ve parola bilgileri ile giriş kontrolü yapınız.
# email = input('email gir :')
# parola = input('parola gir :')

# em = 'hayaller@gmail.com'
# pas = 'and123'

# rs = (email == em) and (parola == pas)
# print('Giriş yapabilirsiniz:', rs)


#Girilen 3 sayıyı büyüklük olarak karşılaştırınız.
# birinci = int(input('birinci sayıyı giriniz:'))
# ikinci = int(input('ikinci sayıyı giriniz:'))
# üçüncü = int(input('üçüncü sayıyı giriniz:'))
# rs = (birinci > ikinci)
# print(birinci, '>', ikinci, ':', rs)
# rs = (ikinci > üçüncü)
# print(ikinci, '>', üçüncü, ':', rs)
# rs = (üçüncü > birinci)
# print(üçüncü, '>', birinci, ':', rs)


# VİZE_FİNAL HESAPLAMA
# vize1 = int(input('vize1 notunu giriniz:'))
# vize2 = int(input('vize2 notunu giriniz:'))
# final = int(input('final notunu giriniz:'))
# ortalama = (vize1 + vize2)/2*0.4 + final *0.6
# print('ortalama:', ortalama)
# rs = (ortalama>50) and (final >=50) or final >=70
# print('geçme durumu:', rs)


# #KİLO İNDEKSİ HESAPLAMA
# kilo = float(input('kilonuz: '))
# boy = float(input('boyunuz: '))
# index = kilo / (boy **2)
# zayıf = index <=  18.4 and index > 0
# normal = index >= 18.5 and index <= 24.9
# kilolu = index >= 25 and index <= 29.9
# obez = index >= 30 and index <= 39.9
# print('zayıf:', zayıf)
# print('normal:', normal)
# print('kilolu:', kilolu)
# print('obez:', obez)