def char_frequency(s):
    frequency = {}

    for c in s:
        frequency[c] = frequency.get(c, 0) + 1

    return frequency


print(char_frequency("Hello World"))
