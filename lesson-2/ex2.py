data = int(input('number '))
numbers= list()
count=1
for i in range(1,data+1):
    count *= i
    numbers.append(count)
print(numbers)