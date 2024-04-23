#!/bin/python3

import os

#
# Complete the 'reverseArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#


def reverseArray(a):
    # Write your code here
    n = len(a)
    mid = len(a) // 2

    for i in range(mid):
        a[i], a[n - i - 1] = a[n - i - 1], a[i]
    return a


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    fptr.write(" ".join(map(str, res)))
    fptr.write("\n")

    fptr.close()
