# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
def create_fi():
    num=list(range(int(input('get number '))))
    plus = [0]
    minus=[]
    result=[]
    num1=1
    num2=0
    sum = 0
    for i in num:
      sum = num1+num2
      plus.append(sum)
      num1=num2
      num2 =sum
    for i in plus:  
        minus.append(plus[i]*(-1))
        print(minus)
    result.extend(minus)
    result.extend(plus)
    print(result)
    print(num)
    print(plus)
    print(minus)
    
create_fi()