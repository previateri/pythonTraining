import random

def list_generate(size):
    list = []
    for i in range(size):
        list.append(random.randint(0, size))
    return list