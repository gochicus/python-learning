#Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
#Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
from random import random
def get_rest(get_numbers):
     result =[]
     counter = 0
     while counter < len(get_numbers):
        rest = get_numbers[counter] - int(get_numbers[counter])
        result.append(rest)
        counter+=1
     return result
def get_float():
    base = list(range(int(input('get number '))))
    result = []
    for i in base:
       get_random=random()*10 
       result.append(get_random)
    return result
def get_max(counter,max,rest):
      while counter < len(rest)-1:
        if max < rest[counter]:
            max= rest[counter]
            counter+=1
        else:
            max = max
            counter+=1
      return max
def get_min(counter,min,rest):
      while counter < len(rest)-1:
        if min > rest[counter]:
            min= rest[counter]
            counter+=1
        else:
            min = min
            counter+=1
      return min
def find_diff():
    counter = 0
    get_numbers= get_float()
    rest = get_rest(get_numbers)
    min = get_min(counter,rest[0],rest)
    max = get_max(counter,rest[0],rest)
    diff = round(max - min,4)
    
    print(rest)
    print (diff)
    print(max)
    print(min)
    
find_diff()