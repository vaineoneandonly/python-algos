from arrayOperations import swap

def execute(a):
    n = len(a)

    swapped = False
    while (not swapped):
        swapped = True
        
        for i in range(1, n):
            if a[i-1] > a[i]:
                swap(a, i, i-1)
                swapped = False

