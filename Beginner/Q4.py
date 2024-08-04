start = int(input("Enter start number: "))
stop = int(input("Enter stop number: "))

sum = 0
for i in range(start, stop):
    if (i%2 != 0):
        sum += i

print(f"Sum of odd numbers: {sum}")