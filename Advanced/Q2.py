number_of_lines = 0

with open(r'demo.txt', 'r') as file:
    lines = len(file.readlines())

    for line in file:
      number_of_lines += 1

print(number_of_lines)