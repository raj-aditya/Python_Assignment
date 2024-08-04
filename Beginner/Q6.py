num = int(input("Enter number: "))
perfect_sum = 0
for i in range(1, num):
    if (num%i == 0):
        perfect_sum += i
if perfect_sum == num:
    print("Yes")
else:
    print("No")