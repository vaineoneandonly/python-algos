import random

def fill(a, n, min, max):
    for i in range(n):
        newVal = random.randint(min, max)
        a.append(newVal)