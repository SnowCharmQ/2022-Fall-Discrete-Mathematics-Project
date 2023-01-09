from utils import *
from prime_generator import Generator


def generate_keypair(p, q):
    # Generate the public key and the private key
    n = p * q
    phi = (p - 1) * (q - 1)
    # Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)
    # Use Euclidean algorithm to verify that e and phi(n) are coprime
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
    # Use Extended Euclidean algorithm to generate the private key
    d = find_mod_inverse(e, phi)
    # Return public and private keypair
    # Public key is (e, n) and private key is (d, n)
    return (e, n), (d, n)


def encrypt(pk, plaintext):
    # Encrypt the plaintext using the public key
    key, n = pk
    cipher = [(ord(char) ** key) % n for char in plaintext]
    return cipher


def decrypt(pk, ciphertext):
    # Decrypt the ciphertext using the private key
    key, n = pk
    plain = [chr((char ** key) % n) for char in ciphertext]
    return ''.join(plain)


if __name__ == '__main__':
    print("RSA Encryption and Decryption")
    g = Generator()
    p = g.generate()
    q = g.generate()
    while p == q:
        p, q = g.generate(), g.generate()
    print("Generating your public/private keypairs now . . .")
    print("Two prime numbers: ", p, q)
    public, private = generate_keypair(p, q)
    print("Your public key is ", public, " and your private key is ", private)
    message = input("Enter a message to encrypt with your public key: ")
    encrypted_msg = encrypt(public, message)
    print("Your encrypted message is: ")
    print(encrypted_msg)
    print("Decrypting message with private key . . .")
    print("Your message is:")
    print(decrypt(private, encrypted_msg))
