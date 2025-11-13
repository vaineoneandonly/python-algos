from arrayOperations import swap

import quickSort

def execute(a):
    bucketSortStep(a, 8)

def bucketSortStep(a, k):
    buckets = []

    maxNum = -1
    for n in a:
        if (n > maxNum):
            maxNum = n
    M = 1 + maxNum

    step = M // k
    
    for i in range(0, k):
        buckets.append([])

    for key in a:
        res = int((key / maxNum) * maxNum)
        idx = (res // step)

        if (idx > 0): idx -= 1

        buckets[idx].append(key)

    n = len(buckets)
    for i in range(0, n-1):
        nn = len(buckets[i])
        quickSort.execute(buckets[i])
        #for j in range(0, nn-1):
        #    print(buckets[i][j])
        #print(buckets[i])