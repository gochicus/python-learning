numb = int(input("Введите целое число: "))
print("Простые:", end = " ")
for i in range(numb - 1, 1, -1):
    is_simple = 0
    if (numb % i == 0):
        for j in range(i - 1, 1, -1):
            if (i % j == 0):
                is_simple = is_simple + 1 
        if (is_simple == 0): 
            print(i, end = " ")