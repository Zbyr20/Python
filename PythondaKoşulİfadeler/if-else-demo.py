# Ehliyet alma yasi kontrolu
# name = input('İsminizi giriniz: ')
# last_name = input('Soyisminizi giriniz: ')
# age = int(input('yasınızı giriniz: '))

# if age >= 18:
    # print(f'{name} {last_name} 18 yasından büyüksün rahat ol!!')
# elif age < 18:
    # print(f'{name} {last_name} 18 yasından kücüksün üzülme!!')


# exam_1 = int(input('Birinci yazılı notunu gir'))
# exam_2 = int(input('İkinci yazılı notunu gir'))
# quiz = int(input('Sözlü notunu gir'))
# ortalama = (exam_1 + exam_2 + quiz) / 3
# if ortalama >= 0 and ortalama <= 24:
    # print(f'Not ortalamanız {ortalama} ve notunuz 0 ')
# elif ortalama >= 25 and ortalama <= 45:
    # print(f'Not ortalamanız {ortalama} ve notunuz 1 ')
# elif ortalama >= 46 and ortalama <= 54:
    # print(f'Not ortalamanız {ortalama} ve notunuz 2 ')
# elif ortalama >= 55 and ortalama <= 69:
    # print(f'Not ortalamanız {ortalama} ve notunuz 3 ')
# elif ortalama >= 70 and ortalama <= 84:
    # print(f'Not ortalamanız {ortalama} ve notunuz 4 ')
# elif ortalama >= 85 and ortalama <= 100:
    # print(f'Not ortalamanız {ortalama} ve notunuz 5 ')

import datetime

# simdi = datetime.datetime.now()
# print(simdi.year)
# print(simdi.strftime('%A'))  # Gün ismini verir

# cikis = datetime.datetime(int(input('Yıl: ')), int(input('Ay: ')), int(input('Gün: ')))
# gun_farki = datetime.datetime.now() - cikis
# print(gun_farki.days)


# tarih = input('Tarihi giriniz: ')
# tarih = tarih.split('/')
# trafige_cikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
# now = datetime.datetime.now()
# yıl_farki = now - trafige_cikis
# days = yıl_farki.days
# print(days)


# tarih = input('Tarihi giriniz: ') 
# tarih = tarih.split('/') 
# tarih = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
# print(tarih)

yazili_1 = float(input('Birinci yazili notunu giriniz: '))
yazili_2 = float(input('İkinci yazili notunu giriniz: '))
sözlü_1 = float(input('Birinci sözlü notunu giriniz: '))

ortalama = (yazili_1 + yazili_2 + sözlü_1) / 3 
print(f'Ortalamanız: {ortalama}')


if ortalama >= 0 and ortalama < 24:
    print('Notunuz: 0')
elif ortalama >= 24 and ortalama < 44:
    print('Notunuz: 1')
elif ortalama >= 44 and ortalama < 54:
    print('Notunuz: 2')
elif ortalama >= 55 and ortalama < 70:
    print('Notunuz: 3')
elif ortalama >= 70 and ortalama < 85:
    print('Notunuz: 4')
elif ortalama >= 85 and ortalama <= 100:
    print('Notunuz: 5')