content = ''
with open(r'demo.txt', 'r') as file:
    content = file.read()

print(content.replace('J', 'I'))

