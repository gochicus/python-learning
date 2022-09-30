from unittest import result


x = int(input('x'))
y = int(input('y'))

x1 = int(input('x1'))
y1 = int(input('y1'))

sqr1 = (x1-x)**2
sqr2 = (y1-y)**2

result = (sqr1 + sqr2)/0.5
print(result)