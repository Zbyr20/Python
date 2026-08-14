import random

# 0 ile 1 arasında rastgele sayı (ondalıklı)
# print(random.random())

# Belirli aralıkta rastgele tam sayı
# print(random.randint(1, 10))  # 1 ile 10 arasında

# Belirli aralıkta rastgele ondalıklı sayı
# print(random.uniform(1, 10))  # 1.0 ile 10.0 arasında

x = random.randint(1,100)
hak = 5
hak = int(input('Kaçta bilirsin? '))
girdi = 0
sayac = 0
while hak >0:
    sayac += 1
    girdi = int(input('Tahmin et bakalım'))
    hak-=1
    if girdi == x:
        print(f'Doğru bildin {x} {sayac}. da puanın: {100-(100/hak)*(sayac-1)}')
        break
    elif girdi >x:
        print('asagı')
    else:
        print('yukarı')
    if hak ==0:
        print(f'Hakkınız bitt. Cevap: {x}')
        