from arrayOperations import swap


def execute(a):
    n = len(a)
    quickSortStep(a, 0, n-1)

def quickSortStep(a, lo, hi):
    if (lo >= hi or lo < 0):
        return
    
    p = partition(a, lo, hi)
    
    quickSortStep(a, lo, p-1)
    quickSortStep(a, p+1, hi)

def partition(a, lo, hi):
    pivot = a[hi]

    i = lo
    for j in range(lo, hi-1):
        if a[j] <= pivot:
            swap(a, a[j], a[i])
            i += 1

    swap(a, a[i], a[hi])   

    return i