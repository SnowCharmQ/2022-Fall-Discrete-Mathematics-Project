from utils import *


def crack(c1, c2, e1, e2, n):
    s1, s2, _ = extended_euclidean(e1, e2)
    if s1 < 0:
        s1 = -s1
    if s2 < 0:
        s2 = -s2
    c1 = find_mod_inverse(c1, n)
    c2 = find_mod_inverse(c2, n)
    m = (((c1 ** s1) % n) * ((c2 ** s2) % n)) % n
    return chr(m)


n = int(input("Enter the modulo n: "))
e1 = int(input("Enter the public key e1: "))
e2 = int(input("Enter the public key e2: "))
c1 = int(input("Enter the number of the encrypted character c1: "))
c2 = int(input("Enter the number of the encrypted character c2: "))
m = crack(c1, c2, e1, e2, n)
print("Successfully crack the character:", m)
