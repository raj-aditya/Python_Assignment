names =  ['Sam', 'Alice', 'Mona']
subjects = ['Commerce', 'Science', 'Computer']

dict = {}

for name, subject in zip(names, subjects):
    dict[name] = subject

print(dict)