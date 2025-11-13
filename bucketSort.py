from arrayOperations import findMax

import quickSort

def execute(a):
    bucketSortStep(a, 10)

def bucketSortStep(a, k):
    buckets = []

    step = (1 + findMax(a)) // k
    
    for i in range(0, k):
        buckets.append([])

    for key in a:
        idx = (key // step)

        if (idx > 0): idx -= 1

        buckets[idx].append(key)

    n = len(buckets)
    for i in range(0, n-1):
        quickSort.execute(buckets[i])
    
    a.clear()

    for bucket in buckets:
        for key in bucket:
            a.append(key)
            