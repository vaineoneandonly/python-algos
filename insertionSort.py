from arrayOperations import swap, executeVisualStep

def execute(a):
    n = len(a)

    i = 1
    executeVisualStep(a)
    while i < n:
        executeVisualStep(a)
        j = i
        while j > 0 and a[j-1] > a[j]:
            swap(a, j-1, j)
            j -= 1
        
        i += 1
    executeVisualStep(a)

