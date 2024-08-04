zero_count = 0
s = input("Enter String: ")

parts = s.split('0')

new_list=[x for x in parts if len(x)>0]

dict = {}

for n in range(len(new_list)):
    if n == 0:
        dict["first_name"] = new_list[0]
    if n == 1:
        dict["last_name"] = new_list[1]
    if n == 2:
        dict["id"] = new_list[2]

print(dict)



