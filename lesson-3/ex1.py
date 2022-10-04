#1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
#Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
from random import random

def get_random():
   count = list(range(int(input('get number '))))
   result=[]
   for i in count:
       result.append(int(random()*100))
   return result  
# Выбираем чётные по индексам, получаем нечётные по позиции 
def get_odd():
    list=get_random()
    list_odd = []
    counter= 0
    while counter<= len(list)-1:
        if counter%2==0:
            list_odd.append(list[counter])
        counter+=1
    return list_odd

def get_odd_sum():
    list = get_odd()
    result = 0
    counter= 0
    while counter<= len(list)-1:
         result+=list[counter]
         counter+=1
    print(result)
    
get_odd_sum()