import random


def gcd(a, b):
    # Euclidean algorithm for finding GCD
    while b != 0:
        a, b = b, a % b
    return a


def find_mod_inverse(a, m):
    # Extended Euclidean algorithm for finding modular inverse
    m0 = m
    y = 0
    x = 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        t = m
        m = a % m
        a = t
        t = y
        y = x - q * y
        x = t
    if x < 0:
        x = x + m0
    return x


def miller_rabin(p):
    if p == 1:
        return False
    if p == 2:
        return True
    if p % 2 == 0:
        return False
    m, k, = p - 1, 0
    while m % 2 == 0:
        m, k = m // 2, k + 1
    a = random.randint(2, p - 1)
    x = pow(a, m, p)
    if x == 1 or x == p - 1:
        return True
    while k > 1:
        x = pow(x, 2, p)
        if x == 1:
            return False
        if x == p - 1:
            return True
        k = k - 1
    return False


def is_prime(p, r=40):
    for _ in range(r):
        if not miller_rabin(p):
            return False
    return True


def extended_euclidean(a, b):
    if b == 0:
        return 1, 0, a
    else:
        x, y, q = extended_euclidean(b, a % b)
        x, y = y, x - (a // b) * y
        return x, y, q
