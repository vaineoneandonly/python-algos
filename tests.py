import bubbleSort
import insertionSort
import selectionSort
import quickSort
import bucketSort

import arrayOperations

import os
import time
import multiprocessing

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
    arrayOperations.fill(a, 10000, 0, 100)
    
    sequentialTests()
    parallelTests()