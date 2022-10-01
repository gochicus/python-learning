float = float(input('float'))
num = int(float)
rest = float - num
st1= str(num)
str2 = str(rest)
counter = 0

for i in st1:
   counter +=  int(i)  

for i in str2:
    if i!='.':
        counter +=  int(i)
print(counter)

