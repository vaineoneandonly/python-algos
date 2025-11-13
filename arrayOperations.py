import random
import copy
import time
import os

def fill(a, n, min, max):
    for i in range(n):
        newVal = random.randint(min, max)
        a.append(newVal)

#will monkey patch this later.
def monkeyPatch_runTest(self, method):
    ca = copy.copy(self)

    print(f"executing {method.__name__} for array below: \n{ca}\n")

    t1 = time.perf_counter()
    method.execute(ca)
    t2 = time.perf_counter()
    
def runTest(a, method):
    ca = copy.copy(a)

    os.system("clear")
    print(f"executing {method.__name__} for array below: \n{ca}\n")

    t1 = time.perf_counter()
    method.execute(ca)
    t2 = time.perf_counter()

    print(f"elapsed time: {t2 - t1}\n\nresult: \n{ca}\n")

def swap(a, i, j):
    a[i], a[j] = a[j], a[i]