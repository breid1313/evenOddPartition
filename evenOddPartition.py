import random
import argparse

def createArray(min, max, size):
    print("Initializing the input array...\nMax integer value: {}\nMin integer value: {}\nArray size: {}".format(max, min, size))
    A = []
    for i in range(0, size):
        n = random.randint(min, max)
        A.append(n)
    print("Input array: {}".format(A))
    return A

def swapPositions(list, pos1, pos2): 
      
    list[pos1], list[pos2] = list[pos2], list[pos1] 
    return list

def partitionEvenOdd(A, n):
    print("Sorting the array...")
    lastEven = -1
    for i in range(0, n):
        if A[i] % 2 == 0:
            if lastEven != (i-1):
                swapPositions(A, i, lastEven + 1)
            lastEven = lastEven + 1
    print("Sort complete.\nPartitioned array: {}".format(A))


if __name__ == "__main__":
    # initialize a parser
    parser = argparse.ArgumentParser()

    # add args to the parser
    parser.add_argument("-m", "--min", type=int, help="minimum value allowed for the integer array")
    parser.add_argument("-M", "--max", type=int, help="maximum value allowed for the integer array")
    parser.add_argument("-s", "--sample-size", dest="size", type=int, help="size of the input array")

    # parse the arguments
    args = parser.parse_args()

    # create and partition the array
    A = createArray(args.min, args.max, args.size)
    partitionEvenOdd(A, len(A))
