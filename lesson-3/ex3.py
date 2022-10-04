def binary_transition():
    n = int(input('number'))
    b = ''
 
    while n > 0:
     b = str(n % 2) + b
     n = n // 2
 
    print(b)
            
binary_transition()