from arrayOperations import swap

def execute(a):
    n = len(a)

    i = 1
    while i < n:
        j = i
        while j > 0 and a[j-1] > a[j]:
            a[j]
