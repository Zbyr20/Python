girdi = int(input('bir sayı giriniz: '))
asalMi = True
if girdi == 1:
    print('sayı asal değildir')
for i in range(2,girdi):
    if girdi% i == 0:
        asalMi = False
        break

if asalMi == True:
    print('sayı asal')
else:
    print('sayi asal değil')