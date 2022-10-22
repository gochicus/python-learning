data = [5,5,6,7,3,4,4,5,7,8,9,9,3,5,3]

def condition(num,list):
    rep = []
    for i in list:
        if i == num:
         rep.append(num)
         while len(rep) >1:
             list.remove(num)
             rep.remove(i)
             print(list) 
    """ if num/num == 1:
      res = list.remove(num)
      return res """
  
def check(numbers):
    for x in numbers:
        result =  list(filter(condition(data[x],data),data))
        print(result) 

check(data)
        
