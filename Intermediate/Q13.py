s = input("Enter String: ").lower()

start_with = lambda x: True if x[0]=='h' else False

print(start_with(s))