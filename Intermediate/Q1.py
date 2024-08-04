L1= [1,2,3,4,5]
L2= [4,5,6,7,8]

result = []

for i in L1:
    if i in L2:
        result.append(i)

print(result)