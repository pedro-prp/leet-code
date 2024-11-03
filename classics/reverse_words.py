def reverse_words(phrase):

    words = phrase.split()

    reversed_words = words[::-1]

    return " ".join(reversed_words)


print(reverse_words('Hello World from Reverse'))
