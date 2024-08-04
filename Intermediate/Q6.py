
num = int(input("Enter Number: "))

def recursion(pow):

    if (2**pow == num):
        return "Yes"
    elif (2**pow > num):
        return "No"
    return recursion(pow+1)


print(recursion(1))