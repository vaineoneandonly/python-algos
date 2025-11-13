import bubbleSort

import arrayOperations

if (__name__ == "__main__"):
    a = []
    arrayOperations.fill(a, 100, 0, 10)
    print(a)
    bubbleSort.execute(a)
    print(a)
