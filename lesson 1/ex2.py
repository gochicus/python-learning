for x in range(0,1):
    for y in range(0,1):
        for z in range(0,1):
           print(not(x or y or z) == (not x or not y or not z)) 