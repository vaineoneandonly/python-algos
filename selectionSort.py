from arrayOperations import swap, executeVisualStep

def execute(a):
    n = len(a)

    for i in range(0, n-1):
        executeVisualStep(a)
        idxOfMin = i
        for j in range(i+1, n):
            if (a[j] < a[idxOfMin]):
                idxOfMin = j

        if idxOfMin != i:
            swap(a, i, idxOfMin)
    
    executeVisualStep(a)
    