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


def try_division(n):
    # Trying division method for finding factors of n
    if n == 1:
        return 1
    if n % 2 == 0:
        return 2
    for i in range(2, n + 1):
        if n % i == 0:
            return i
    return n


def pollard_rho(n):
    # Pollard's Rho Algorithm for finding factors of n
    if n == 1:
        return 1
    if n % 2 == 0:
        return 2
    x = (random.randrange(3, n - 1) % (n - 3)) + 2
    c = (random.randrange(3, n - 1) % (n - 3)) + 2
    y = x
    k = 1
    while True:
        x = ((x * x) % n + c) % n
        d = gcd(n, abs(y - x))
        if d != 1:
            return d
        if y == x:
            return n
        k = k * 2
        if k == y:
            y = x


def attack_brute_force(ciphertext, e, n):
    # Decrypt the ciphertext using brute-force attack and Pollard's Rho Algorithm
    p = pollard_rho(n)  # pollard_rho or try_division
    q = n // p
    phi = (p - 1) * (q - 1)
    d = find_mod_inverse(e, phi)
    return [(char ** d) % n for char in ciphertext]


def decrypt_message(ciphertext, e, n):
    # Decrypt the ciphertext and return the original message
    plaintext = [chr(i) for i in attack_brute_force(ciphertext, e, n)]
    return ''.join(plaintext)


if __name__ == '__main__':
    # Test the decrypt function
    ciphertext = [115, 298, 93, 187, 63, 270, 71, 190, 79]
    e = 277
    n = 323
    print(decrypt_message(ciphertext, e, n))
