import random


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


class Generator:

    def __init__(self):
        self.index = 12

    def generate(self):
        num = 0
        for i in range(self.index):
            num = num * 2 + random.randint(0, 1)
        while not is_prime(num):
            num = num + 1
        return num
