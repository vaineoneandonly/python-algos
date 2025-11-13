import bubbleSort
import insertionSort
import selectionSort

import arrayOperations

import os

if (__name__ == "__main__"):
    os.system("clear")
    a = []

    arrayOperations.fill(a, 10000, 0, 100)
    arrayOperations.runTest(a, bubbleSort)
    #would have preferred to monkey patch. maybe in the future.
    
    arrayOperations.runTest(a, insertionSort)
    arrayOperations.runTest(a, selectionSort)
