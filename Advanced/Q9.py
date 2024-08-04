s = input("Enter String:")

current_char = s[1]
encoded_string = ''
count = 1

for c in s[1::]:
    if c == current_char:
        count += 1
    else:
        encoded_string += current_char + str(count)
        current_char = c
        count = 1

encoded_string += current_char + str(count)


print(encoded_string)