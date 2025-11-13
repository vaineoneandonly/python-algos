import bubbleSort

import arrayOperations

if (__name__ == "__main__"):
    a = []

    arrayOperations.fill(a, 100, 0, 100)
    arrayOperations.runTest(a, bubbleSort)
    #would have preferred to monkey patch. maybe in the future.
    