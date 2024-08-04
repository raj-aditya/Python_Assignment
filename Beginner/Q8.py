num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))

gcd = 1
temp1 = num1
temp2 = num2

while temp2:
    temp1, temp2 = temp2, temp1%temp2
gcb = temp1
print ((num1*num2)//gcb)