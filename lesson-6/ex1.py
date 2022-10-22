data = [15, 16, 2, 3, 1, 7, 5, 4, 10]
def check(list):
  i = 0
  result = []
  while i < len(list):
     if list[i]!=list[0] and list[i] > list[i-1]: 
        result.append(list[i])
        print(result)
     i+=1
  return result  

print(check(data))

