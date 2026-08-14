# sayilar =[1,3,5,7,9,12,19,21]
# toplam =0
# for s in sayilar:
    # if s%3 ==0:
        # print(f"{s} sayisi 3'ün katıdır")
    # toplam +=s
# print(toplam)
# print("***************************")

# for h in sayilar:
    # if h%2 ==1:
    #  print(h**2)








# sehirler = ['kocaeli' , 'istanbul' , 'ankara' , 'izmir' , 'rize']

# for s in sehirler:
    # if len(s)<=5:
        # print(s)


urunler = [
    {'name': 'samsung S6','price' : '3000'},
    {'name': 'samsung S7','price' : '4000'},
    {'name': 'samsung S8','price' : '5000'},
    {'name': 'samsung S9','price' : '6000'},
    {'name': 'samsung S10','price' : ' 7000'}
]
# top =0
# for x in urunler:
    #  top += int(x['price']) 
# print(top)

for x in urunler:
    if int(x['price']) <= 5000:
        print(x['name'])