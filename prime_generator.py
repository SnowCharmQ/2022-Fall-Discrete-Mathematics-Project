from utils import *


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
