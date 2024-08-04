list = [1,2,3,4,5]

k = 6

dict = {}

count = 0

for i in list:
    dif = k - i
    if dif in dict:
        count += 1
    else:
        dict[i] = dif

print(count)