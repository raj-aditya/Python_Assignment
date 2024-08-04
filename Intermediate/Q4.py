list = [1,2,3,4,5]

d = 2
d = d % len(list)

rotated_array = list[-d:] + list[:-d]
print(rotated_array)