s = input("Enter String:").lower()

vowel = ['a', 'e', 'i', 'o', 'u']
count = 0
for c in s:
    if c in vowel:
        count += 1

print(count)

