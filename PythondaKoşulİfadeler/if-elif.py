# x=3
# y=4
# a = y
# y = x
# x = a
# if x>y:
    # print(f"{x} is greater than {y}")
# elif x<y:
    # print(f"{x} is less than {y}")
# else:
    # print(f"{x} is equal to {y}")


num =int(input('Bir sayi giriniz: '))
if num>0:
    print(f'{num} sayisi pozitif bir sayidir')
elif num<0:
    print(f'{num} sayisi negatif bir sayidir')
else:
    print(f'{num} sayisi ne pozitif ne de negatif bir sayidir')
