# mumUzunluğu= 120
# kalanMum1= mumUzunluğu
# kalanMum2 = mumUzunluğu
# saatteHız1 = 40
# saatteHız2 = 20
# saat = 0
# while kalanMum2 != 2*kalanMum1:
#         kalanMum1 = kalanMum1 - saatteHız1
#         kalanMum2 = kalanMum2 - saatteHız2
#         saat = saat +1
# print(saat)  


# saatteHız1 = 18
# saatteHız2 = 25
# pistinUzunluğu = int
# saat = 1
# while (saatteHız1*saat)*5 != (saatteHız2*saat)*3 +30:
#     saat = saat + 1
# print(saat)
# pistinUzunluğu= (saat*saatteHız1)/3
# print(pistinUzunluğu)

saatteHız1 = 80 
saatteHız2 = 100
saat = 0
while saat < 7:
    saat = saat +1
    if saat % 3 ==0:
        saat = saat + 0.5
    aldığıYol = saat*saatteHız1
print(aldığıYol)
print(saat)