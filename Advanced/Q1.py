number_of_even_words = 0

with open(r'doc.txt', 'r') as file:

    data = file.readline()

    words = data.split()
    for word in words:
        if len(word)%2 == 0:
            number_of_even_words += 1


print(number_of_even_words)