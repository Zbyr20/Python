# def isteGöster(word:str,hm:int):
#     print(hm*word)
# isteGöster("ben\n",2)

# def listeyeCevir(*params):
#     liste = []
#     for param in params:
#         liste.append(param)
#     return liste
# result = listeyeCevir("Elma","Armut")
# print(result)



# def asalıBul(ilkSayi,ikinciSayi):
#     x= ilkSayi
#     asalMi= True
#     while x < ikinciSayi:
#         y = 1
#         while y < 10:
#             if x %y ==0: 
#                 asalMi =False
#             y = y+1
#         print(x + asalMi)
        
       

# asalıBul(2,15)



# def asalSayılariBul(sayi1, sayi2):
#     for sayi in range(sayi1,sayi2+1):
#         if sayi > 1:
#             for i in range(2, sayi):
#                 if sayi % i == 0 :
#                     break
#                 else:
#                     print(sayi)

# sayi1 = int(input('sayı 1:'))
# sayi2 = int(input('sayı 2:'))
# asalSayılariBul(sayi1,sayi2)


# sayi = int(input("sayi gir:"))
# def tamBolenlers(sayi):
#     tamBolenler = []
#     for i in range(2, sayi):
#         if (sayi % i == 0):
#             tamBolenler.append(i)
#     return tamBolenler
# print(tamBolenlers(sayi))