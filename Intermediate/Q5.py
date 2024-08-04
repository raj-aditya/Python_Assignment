list = [25,28,21,24,27]

high_temp = 0
low_temp = float("inf")
sum = 0
for temp in list:
    if (temp > high_temp):
        high_temp = temp
    if (temp<low_temp):
        low_temp = temp
    sum = sum+temp


print(f"Average: {sum//len(list)} High: {high_temp}, Low: {low_temp}")
