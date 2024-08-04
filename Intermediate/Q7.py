list = [7,2,5,1,9,3]


list = sorted(list)
n = len(list)

if n%2 == 1:
    print(list[n//2])
else:
    a = list[n//2 - 1]
    b = list[n//2]
    print((a+b)/2)

