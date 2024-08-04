s = input("Enter String: ")

n = input("Enter Computer Count: ")

arr = []

return_count = 0
returned_user = []

for c in s:
    if len(arr) == n and c not in arr and c not in returned_user:
        returned_user.append(c)
        return_count += 1
    else:
        if c not in arr:
            arr.append(c)
        else:
            arr.remove(c)
print(return_count)