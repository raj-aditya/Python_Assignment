list = [1,2,3,2,4,1,2,4,5]

dict = {}

for i in list:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
print(dict)