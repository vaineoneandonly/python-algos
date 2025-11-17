from arrayOperations import swap, executeVisualStep

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
    for j in range(lo, hi):
        if a[j] <= pivot:
            swap(a, i, j)
            i += 1

    swap(a, i, hi)   

    return i