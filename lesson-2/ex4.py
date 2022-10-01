from unittest import result


list = [-5,-4,-3,-2,-1,0,1,2,3,4,5]
data1 = int(input('number'))
data2 = int(input('number'))
if data1> len(list) or data2> len(list):
    print('out of range')
else:
    result = list[data1-1] * list[data2-1]
    print(result)