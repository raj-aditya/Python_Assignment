list = [2,4,5,6]

try:
    element = list[5]
    print(element)
except IndexError:
    print("Error: Index out of range")