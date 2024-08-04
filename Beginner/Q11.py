num = int(input("Enter Number: "))
def sumdigit(num):
    sum = 0
    while (num > 0):
        digit = num % 10
        sum += digit
        num = num // 10
    return sum

s = sumdigit(num)
while(s>=10):
    s = sumdigit(s)
print(s)

