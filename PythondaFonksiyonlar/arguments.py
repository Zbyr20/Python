# def changeName(n):
    # n = 'ada'

# name = 'yiğit'


# def change(n):
    # n[0] = 'istanbul'

# sehirler = ['ankara', 'izmir']

# change(sehirler)
# print(sehirler)


# def add(*params):
    # return sum((params))
# print(add(10,20))
# print(add(10,20,30))

#Key and Value
def displayUser(**args):
    for key,value in args.items():
        print('{} is {} '.format(key,value))

displayUser(name = 'Çınar', age = 2, city = 'istanbul')