get_number = int(input('get the number more than 20 '))
list = list(filter(lambda x:not  x%20 or not x%21 ,list(range(20,get_number))))
print(list)