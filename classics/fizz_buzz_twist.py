def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


def fizz_buzz_twist(number):

    result = list()

    for i in range(1, (number + 1)):
        if is_prime(i):
            result.append("Prime")
        elif i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(i)

    return result


print(fizz_buzz_twist(15))

