s  = input("Enter String:")
letters_count = 0
digits_count = 0
for c in s:
    if c.isdigit():
        digits_count += 1
    elif c.isalpha():
        letters_count += 1
print (f"Alphabets:{letters_count} & Numbers: {digits_count}")
