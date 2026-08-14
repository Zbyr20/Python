#Value type
# x = 5 
# y= 25
# x = y
# y = 10
# print(x,y) # y nin üzerinde değişiklilik x i etkilemedi çünkü adresler farklı 
#reference types
a = ['apple', 'banana']
b = ['apple' , 'banana']
a = b
b[0] = 'sakama'
b[1] = 'asakama'
print(a,b)
a[0] = 'kazama'
print(a,b)
# birini diğerine atayıp herhangi birinin üzerinde değişiklilik diğerine yansır, ama birini komple değiştirirsen diğerine yansımaz
a=['kuçuma','kuzuma']
print(a,b)
