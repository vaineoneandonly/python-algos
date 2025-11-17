import random
import copy
import time
import os
import termgraph


def fill(a, n, min, max):
    for i in range(n):
        newVal = random.randint(min, max)
        a.append(newVal)

#will monkey patch this later.
def monkeyPatch_runTest(self, method):
    ca = copy.copy(self)

    print(f"executing {method.__name__} for array...")

    t1 = time.perf_counter()
    method.execute(ca)
    t2 = time.perf_counter()
    
def runTest(a, method, *args):
    ca = copy.copy(a)

    print(f"executing {method.__name__:>5} for array...")

    t1 = time.perf_counter()
    method.execute(ca)
    t2 = time.perf_counter()

    #print(f"elapsed time for {method.__name__:>5}:  {(t2 - t1):.5f}  " + ("|" * int(t2 - t1)))

    return ca

def swap(a, i, j):
    a[i], a[j] = a[j], a[i]

def findMax(a):
    maxNum = -1
    for n in a:
        if (n > maxNum):
            maxNum = n

    return maxNum

def executeVisualStep(a):
    b = [0] * len(a)
    for i in range(0, len(a)):
        b[i] = str(i + 1)

    data = termgraph.Data(a, b)
    chart = termgraph.BarChart(data)

    os.system("clear")
    chart.draw()

    time.sleep(0.06)
    #input("type anything to continue.")
    
