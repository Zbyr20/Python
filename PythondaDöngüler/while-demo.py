# sayilar = [1,3,5,7,9,12,19,21]
# index = 0
# while index <len(sayilar):
    # print(sayilar[index])
    # index+=1

# bas = int(input('başlangıç sayisi: '))
# bit = int(input('bitis sayisi: '))
# index = 0
# while index < len(sayilar):
    # print(sayilar[index])
    # index+=1
# print('-------------------------------------------')
# while index < len(sayilar): 
   
    # if bas <= sayilar[index] and bit >= sayilar[index]:
        # if sayilar[index] %2 == 1:
            # print(sayilar[index])
    # index+=1
# x =0
# while x < 100:
    # print(100-x)
    # x+=1



# numbers = input('5 sayı gir')
# numbers = numbers.split()
# x = 0
# while x < 5:
    # for y in numbers:
        # for z in numbers:
            # if numbers[y] < numbers[z]:
                # h= numbers[y]
                # numbers[y] = numbers[z]
                # numbers[z] = h
    # x+=1
# print(numbers)



# numbers = []
# x = 0
# while x <5:
    # num = int(input(f'{x}. sayıyı girin: '))
    # numbers.append(num)
    # x += 1
# numbers.sort
# print(numbers)

urunler=[]

adet = int(input('kaç adet ürün: '))

index = 0
while index < adet:
    name = input('Ürün adı:')
    price = int(input('Ürün fiyatı: '))
    urunler.append({
        'name' :name,
        'price' : price
    })
    index +=1
# print(urunler)
# print('-----------***********---------------')
# i =0
# while i < len(urunler):
        # print(urunler[i])
        # i+=1
for urun in urunler:
    print(f'ürün adı{urun["name"]} ürün fiyatı: {urun["price"]}')