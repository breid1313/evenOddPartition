import random

def swapPositions(list, pos1, pos2): 
      
    list[pos1], list[pos2] = list[pos2], list[pos1] 
    return list

def partitionEvenOdd(A, n):
    lastEven = -1
    for i in range(0, n):
        if A[i] % 2 == 0:
            if lastEven != (i-1):
                swapPositions(A, i, lastEven + 1)
            lastEven = lastEven + 1

# A = [2,2,1,2,1,2,1,2,1]

A = []
for i in range(0,25):
    n = random.randint(1,100)
    A.append(n)
print(A)
partitionEvenOdd(A, len(A))
print(A)