def prime_factors(value):
    check_prime = check_primality(value)
    if not check_prime:
        multiples = []
        smallest_prime_factor(value, multiples)
        return tuple(multiples)
    else:
        return value


def smallest_prime_factor(value, multiples):
    for number in range(2, value):
        if value % number == 0:
            multiples.append(number)
            return smallest_prime_factor(value // number, multiples)
    multiples.append(value)


def check_primality(value):
    if value <= 3:
        return True

    for number in range(2, value):
        if value % number == 0:
            return False
    return True


prime = prime_factors(69)
print(prime)
