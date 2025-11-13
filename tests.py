import bubbleSort
import insertionSort
import selectionSort
import quickSort
import bucketSort

import arrayOperations

import os

if (__name__ == "__main__"):
    os.system("clear")
    a = []

    arrayOperations.fill(a, 20000, 0, 100)
    #would have preferred to monkey patch. maybe in the future.
    arrayOperations.runTest(a, bucketSort)
    arrayOperations.runTest(a, quickSort)
    arrayOperations.runTest(a, selectionSort)
    arrayOperations.runTest(a, insertionSort)
    arrayOperations.runTest(a, bubbleSort)