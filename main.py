def is_it_prime(n):
    d = 2
    while d < n:
        if n % d != 0:
            d += 1
        else:
            return False
    return True


def get_prime_numbers(fi=200):
    L = list(range(31, fi))
    prime_numbers = []
    for i in L:
        if is_it_prime(i):
            prime_numbers.append(i)
    return prime_numbers