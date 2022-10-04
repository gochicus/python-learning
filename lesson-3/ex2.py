#. Напишите программу, которая найдёт произведение пар чисел списка.
#Парой считаем первый и последний элемент, второй и предпоследний и т.д.
from random import random
def get_numbers():
   count = list(range(1,int(input('get number '))))
   return count  

def list_is_odd(list):
    list=list
    if len(list)%2==0:
        return False
    else:
        return True

def multiply():
    list = get_numbers()
    result=[]
    counter = 0
    check_odd = list_is_odd(list)
    if check_odd is False:
       count_last=-1
       operation_count =len(list)
       while counter<operation_count:
          count=list[counter]*list[count_last]
          result.append(count)
          count_last-=1
          operation_count-=1
          counter+=1
    if check_odd is True:
       count_last=-1
       operation_count =len(list)
       while counter<operation_count and counter+1!=operation_count:
             count=list[counter]*list[count_last]
             result.append(count)
             count_last-=1
             operation_count-=1
             counter+=1
       if len(result)<len(list):
           result.append(list[len(result)])
            
        
    print(list)
    print(result)
    print(len(list))
multiply()