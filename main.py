import random


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


def find_all_dividers(n):
    d = 2
    dividers = set()
    while d <= n:
        if n % d != 0:
            d += 1
        else:
            dividers.add(d)
            d += 1
    return dividers


def find_e(fi):
    flag = True
    while flag == True:
        e = random.choice(range(1000))
        if e % 2 == 0:
            e -= 1
        flag = (bool(find_all_dividers(e) & find_all_dividers(fi)))
    return e


def find_d(e, fi):
    # d - число обратное е по модулю fi => (d * e) % fi = 1
    d = 1
    while (d * e) % fi != 1:
        d += 1
    return d
