import bubbleSort
import insertionSort
import selectionSort
import quickSort
import bucketSort

import arrayOperations

import os
import time
import multiprocessing

import termgraph

allSorts = [bubbleSort, insertionSort, selectionSort, quickSort, bucketSort]

def parallelTests():
    t1 = time.perf_counter()
    processPool = []

    for method in allSorts:
        processPool.append(multiprocessing.Process(target = arrayOperations.runTest, args = (a, method)))

    for process in processPool:
        process.start()

    for process in processPool:
        process.join()

    t2 = time.perf_counter()    

    print(t2 - t1)

def parallelTestsWithPooling():
    with multiprocessing.Pool(4) as pool:
        pool.starmap(arrayOperations.runTest, [(a, bucketSort), (a, quickSort), (a, insertionSort), (a, selectionSort)])

def sequentialTests():    
    t1 = time.perf_counter()

    #would have preferred to monkey patch. maybe in the future.
    for method in allSorts:
        arrayOperations.runTest(a, method)

    t2 = time.perf_counter()    

    print(t2 - t1)

if (__name__ == "__main__"):
    os.system("clear")

    a = []

    num = 80

    b = [0] * num
    arrayOperations.fill(a, num, 0, 1000000)

    for i in range(0, num):
        b[i] = str(i + 1)

    for method in allSorts:
        input(f"executing {method.__name__}")
        na = arrayOperations.runTest(a, method)
        input(f"type anything to continue.")
        os.system("clear")

    #sequentialTests()
    #parallelTests()