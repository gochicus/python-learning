data = int(input('number '))
numbers= list()
count=0
for i in range(1,data+1):
    count += (1 + 1/i)
    numbers.append(round(count,2))
print(numbers)