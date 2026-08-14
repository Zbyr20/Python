#range(başlangıç,bitiş.artışmiktarı)
# for item in range(19,100,3):
    # print(item)


#enumerate

greeting = 'Hello There'

# for letter in enumerate(greeting):
    # print(letter)

list1 = [1,2,3,4,5]
list2 = ['a','b','c','d','e']
list3 = [100,200,300,400,500]
print(list(zip(list1, list2,list3)))
for a,b,c in list(zip(list1, list2,list3)):
    print(a,b,c)