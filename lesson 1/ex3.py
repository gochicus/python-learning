x = int(input('введите целое число'))
y = int(input('введите целое число'))
if x!=0 and y!=0:
    if x>0 and y>0:
        print('первая четверть')
    elif x>0 and y <0:
        print('четвертая четверть')
    elif x<0 and y>0:
        print('вторая четверть')
    elif x<0 and y<0:
        print('третья четверть')
else:
    print('недопустимое число')

