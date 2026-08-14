# numbers = []
# for x in range(10):
    # numbers.append(x)

# print(numbers)

# print("???????????????????????????????????")

# numbers = [x for x in range(10)]
# print(numbers)

# for x in range(10):
    # print(x**2)

# numbers = [x**2 for x in range(10)]
# print(numbers[4])

# numbers =[x*x for x in range(10) if x%3 == 0]
# print(numbers)


myString = 'Hayırdır Gardes'
# myList = []
# for letter in myString:
    # myList.append(letter)
# print(myList)

#daha kolay yolu
# myList = [ letter for letter in myString]
# print(myList)

# years = [1983,1314,2134,2421,4124]
# ages = [5000-year for year in years]
# print(ages)

# result = [x if x%2  else 'TEK' for x in range(1,10)]
# print(result)

result=[]
for x in range(3):
    for y in range(3):
        result.append((x,y))
print(result)

print([(x,y) for x in range(3) for y in range(3)])