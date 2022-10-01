from random import random

def check(number,list):
    if number in list:
        return False
    else:
         return True
list =[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
def func(i,list):
    index = int(random()*10)  
    if index <= len(list)-1:
        cleaner = list[i]
        list[i]= list[index]
        list[index]=cleaner
            
for i in list:
     func(i,list)

print(list)